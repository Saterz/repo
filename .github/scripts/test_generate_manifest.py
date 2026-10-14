#!/usr/bin/env python3
"""Tests for repository manifest generation."""

import json
import os
import shutil
import subprocess
import tempfile
import unittest


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


class GenerateManifestTests(unittest.TestCase):
    def test_generates_per_package_version_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            script = os.path.join(temp_dir, "generate-manifest.sh")
            shutil.copyfile(os.path.join(REPO_ROOT, "generate-manifest.sh"), script)
            package_dir = os.path.join(temp_dir, "packages", "test")
            os.makedirs(package_dir)
            with open(os.path.join(package_dir, ".meta"), "w", encoding="utf-8") as meta:
                meta.write(
                    "id=test\n"
                    "name=Test\n"
                    "version=2.0.0-beta.1\n"
                    "description=Test package\n"
                    "author=Tester\n"
                    "category=wallpapers\n"
                    "platforms=koreader\n"
                    "dependencies=\n"
                    "alpha_version=2.0.0-alpha.2\n"
                    "alpha_published_at=2026-07-24T01:02:03Z\n"
                    "plugin_module=zenos\n"
                    "plugin_module_aliases=zen_ui\n"
                    "source_asset_aliases=zen_ui.koplugin.zip\n"
                    'releases=[{"tag_name":"v2.0.0-beta.1","name":"Beta release",'
                    '"prerelease":true,"assets":[{"name":"test.koplugin.zip",'
                    '"url":"https://example.com/test.koplugin.zip","size":123,'
                    '"digest":"sha256:abc"}]}]\n'
                )
            empty_package_dir = os.path.join(temp_dir, "packages", "empty")
            os.makedirs(empty_package_dir)
            with open(os.path.join(empty_package_dir, ".meta"), "w", encoding="utf-8") as meta:
                meta.write(
                    "id=empty\n"
                    "name=Empty\n"
                    "version=1.0.0\n"
                    "description=Package without release history\n"
                    "author=Tester\n"
                    "category=utility\n"
                    "tags=zen-icon-pack,zenos\n"
                    "platforms=koreader\n"
                    "dependencies=\n"
                )

            subprocess.run(["sh", script], cwd=temp_dir, check=True, capture_output=True)
            with open(os.path.join(temp_dir, "manifest.json"), encoding="utf-8") as manifest:
                packages = {
                    package["id"]: package for package in json.load(manifest)["packages"]
                }
            with open(os.path.join(package_dir, "versions.json"), encoding="utf-8") as versions:
                releases = json.load(versions)["releases"]
            with open(
                os.path.join(empty_package_dir, "versions.json"), encoding="utf-8"
            ) as versions:
                empty_releases = json.load(versions)["releases"]

            package = packages["test"]
            self.assertEqual(package["category"], "wallpapers")
            self.assertEqual(package["versions_url"], "packages/test/versions.json")
            self.assertEqual(package["plugin_module"], "zenos")
            self.assertEqual(package["plugin_module_aliases"], ["zen_ui"])
            self.assertEqual(package["source_asset_aliases"], ["zen_ui.koplugin.zip"])
            self.assertEqual(package["alpha_version"], "2.0.0-alpha.2")
            self.assertEqual(package["alpha_published_at"], "2026-07-24T01:02:03Z")
            self.assertNotIn("releases", package)
            self.assertEqual(releases, [{
                "tag_name": "v2.0.0-beta.1",
                "name": "Beta release",
                "prerelease": True,
                "assets": [{
                    "name": "test.koplugin.zip",
                    "url": "https://example.com/test.koplugin.zip",
                    "size": 123,
                    "digest": "sha256:abc",
                }],
            }])
            self.assertEqual(
                packages["empty"]["versions_url"], "packages/empty/versions.json"
            )
            self.assertEqual(packages["empty"]["category"], "utility")
            self.assertEqual(packages["empty"]["tags"], ["zen-icon-pack", "zenos"])
            self.assertEqual(empty_releases, [])

    def test_icon_packs_require_release_zips_and_preserve_asset_color_booleans(self):
        for include_released in (True, False):
            with self.subTest(include_released=include_released), tempfile.TemporaryDirectory() as temp_dir:
                script = os.path.join(temp_dir, "generate-manifest.sh")
                shutil.copyfile(os.path.join(REPO_ROOT, "generate-manifest.sh"), script)
                metadata = {
                    "a-unreleased": "source_type=source\nsource_url=https://example.com/source.zip\n",
                    "z-no-assets": "source_type=release\n",
                }
                if include_released:
                    metadata["solar"] = (
                        "source_type=release\n"
                        "assets.0.arch=any\nassets.0.asset=colour.zip\n"
                        "assets.0.url=https://example.com/colour.zip\nassets.0.color=true\n"
                        "assets.1.arch=any\nassets.1.asset=mono.zip\n"
                        "assets.1.url=https://example.com/mono.zip\nassets.1.color=false\n"
                    )
                for package_id, fields in metadata.items():
                    package_dir = os.path.join(temp_dir, "packages", package_id)
                    os.makedirs(package_dir)
                    with open(os.path.join(package_dir, ".meta"), "w", encoding="utf-8") as meta:
                        meta.write(f"id={package_id}\nname={package_id}\ncategory=iconpacks\n" + fields)
                    with open(os.path.join(package_dir, "versions.json"), "w") as versions:
                        versions.write('{"releases": []}')
                subprocess.run(["sh", script], cwd=temp_dir, check=True, capture_output=True)
                with open(os.path.join(temp_dir, "manifest.json"), encoding="utf-8") as manifest:
                    packages = json.load(manifest)["packages"]
                self.assertEqual([package["id"] for package in packages], ["solar"] if include_released else [])
                for package_id in ("a-unreleased", "z-no-assets"):
                    self.assertFalse(os.path.exists(os.path.join(temp_dir, "packages", package_id, "versions.json")))
                if include_released:
                    self.assertIs(packages[0]["assets"][0]["color"], True)
                    self.assertIs(packages[0]["assets"][1]["color"], False)
                    meta_path = os.path.join(temp_dir, "packages", "solar", ".meta")
                    with open(meta_path, "a", encoding="utf-8") as meta:
                        meta.write("assets.2.asset=invalid.zip\nassets.2.color=invalid\n")
                    invalid = subprocess.run(["sh", script], cwd=temp_dir, capture_output=True, text=True)
                    self.assertNotEqual(invalid.returncode, 0)
                    self.assertIn("Invalid asset color", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
