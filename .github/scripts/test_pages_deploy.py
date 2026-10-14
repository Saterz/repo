import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest


class PagesArtifactTest(unittest.TestCase):
    def run_wait(self, appears):
        workflow = Path(__file__).parents[1] / "workflows" / "pages-deploy.yml"
        section = workflow.read_text().split("      - name: Wait for Pages artifact\n", 1)[1]
        script = textwrap.dedent(section.split("        run: |\n", 1)[1].split("\n      - name:", 1)[0])
        script = script.replace("${{ github.run_attempt }}", "3")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "state.json"
            state.write_text(json.dumps({"calls": 0, "appears": appears}))
            gh = root / "gh"
            gh.write_text(f"#!{sys.executable}\n" + textwrap.dedent('''\
                import json, os, re, sys
                from pathlib import Path
                path = Path(os.environ["PAGES_TEST_STATE"])
                state = json.loads(path.read_text())
                state["calls"] += 1
                path.write_text(json.dumps(state))
                names = ["github-pages", "github-pages", "github-pages-1", "github-pages-2"]
                if state["appears"] and state["calls"] >= 3:
                    names.append("github-pages-3")
                query = sys.argv[sys.argv.index("--jq") + 1]
                wanted = re.search(r'[.]name == "([^"]+)"', query).group(1)
                print(names.count(wanted))
                '''))
            gh.chmod(0o755)
            sleep = root / "sleep"
            sleep.write_text("#!/bin/sh\nexit 0\n")
            sleep.chmod(0o755)
            result = subprocess.run(["bash", "-e", "-c", script], capture_output=True, text=True,
                                    env=dict(os.environ, PATH=str(root) + os.pathsep + os.environ["PATH"],
                                             PAGES_TEST_STATE=str(state), GITHUB_REPOSITORY="owner/repo", GITHUB_RUN_ID="123"))
            return result, json.loads(state.read_text())["calls"]

    def test_waits_for_current_attempt_and_ignores_older_artifacts(self):
        result, calls = self.run_wait(True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls, 3)

    def test_fails_when_current_artifact_never_appears(self):
        result, calls = self.run_wait(False)
        self.assertNotEqual(result.returncode, 0)
        self.assertGreater(calls, 1)
