import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest


class DiscordNotificationTest(unittest.TestCase):
    def notify(self, webhook, status="success", curl_status=0):
        script = Path(__file__).with_name("notify-discord.sh")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request = root / "request.json"
            curl = root / "curl"
            curl.write_text(f"#!{sys.executable}\n" + textwrap.dedent('''\
                import json, os, sys
                from pathlib import Path
                Path(os.environ["DISCORD_TEST_REQUEST"]).write_text(json.dumps({
                    "args": sys.argv[1:], "payload": json.load(sys.stdin),
                }))
                sys.exit(int(os.environ["DISCORD_TEST_CURL_STATUS"]))
                '''))
            curl.chmod(0o755)
            result = subprocess.run(["sh", str(script)], capture_output=True, text=True,
                                    env=dict(os.environ, PATH=str(root) + os.pathsep + os.environ["PATH"],
                                             DISCORD_TEST_REQUEST=str(request),
                                             DISCORD_TEST_CURL_STATUS=str(curl_status),
                                             DISCORD_WEBHOOK_URL=webhook, WORKFLOW_STATUS=status,
                                             GITHUB_REPOSITORY="owner/repo", GITHUB_WORKFLOW='Deploy "catalog" @everyone',
                                             GITHUB_SERVER_URL="https://github.com", GITHUB_RUN_ID="123"))
            return result, json.loads(request.read_text()) if request.exists() else None

    def test_sends_one_json_message_with_status_and_run_link(self):
        base = "https://discord.com/api/webhooks/test/token"
        for suffix in ("", "/github"):
            for status in ("success", "failure", "cancelled"):
                with self.subTest(suffix=suffix, status=status):
                    result, request = self.notify(base + suffix, status)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(request["args"][-1], base)
                    self.assertIn("--fail", request["args"])
                    self.assertIn("--max-time", request["args"])
                    self.assertEqual(request["payload"], {
                        "content": f'[owner/repo] Deploy "catalog" @everyone: {status}\n'
                                   "https://github.com/owner/repo/actions/runs/123",
                        "allowed_mentions": {"parse": []},
                    })

    def test_skips_missing_secret_without_sending(self):
        result, request = self.notify("")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNone(request)
        self.assertIn("::warning::", result.stdout)

    def test_delivery_error_is_reported(self):
        result, request = self.notify("https://discord.com/api/webhooks/test/token", curl_status=22)
        self.assertEqual(result.returncode, 22, result.stderr)
        self.assertIsNotNone(request)
