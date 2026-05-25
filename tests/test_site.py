import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class PortfolioSiteTests(unittest.TestCase):
    def test_required_files_exist(self):
        for path in [
            "index.html",
            "styles.css",
            "assets/docs/Raymond_Mokolo_CV.pdf",
            "assets/projects/powerplan.png",
            "assets/projects/panelcheck.png",
            "assets/projects/gridfault.png",
            "assets/projects/maintenance.png",
            "assets/projects/smartbill.png",
            "assets/projects/powerguard.png",
            "assets/projects/switchitup.png",
        ]:
            self.assertTrue((ROOT / path).exists(), path)

    def test_project_links_are_present(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for repo in [
            "PowerPlan-Pro",
            "PanelCheck-Pro",
            "GridFault-Analyst",
            "MaintenanceMind-CMMS",
            "SmartBill-Analyzer",
            "PowerGuard-IoT",
            "SwitchItUp",
        ]:
            self.assertIn(f"https://github.com/Raywizzy/{repo}", html)
            self.assertIn(f"https://raywizzy.github.io/{repo}/", html)

    def test_images_have_alt_text(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        images = re.findall(r"<img [^>]+>", html)
        self.assertGreaterEqual(len(images), 6)
        for image in images:
            self.assertIn("alt=", image)


if __name__ == "__main__":
    unittest.main()
