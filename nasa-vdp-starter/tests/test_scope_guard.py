"""Offline unit tests. Run: python -m unittest discover -s tests -v"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scope_guard import get_hostname, is_allowed, load_exact_hosts


class ScopeGuardTests(unittest.TestCase):
    def test_empty_scope_denies(self):
        self.assertFalse(is_allowed("https://example.org/", set()))

    def test_exact_host_only(self):
        scopes = {"example.org"}
        self.assertTrue(is_allowed("https://example.org/profile", scopes))
        self.assertTrue(is_allowed("https://EXAMPLE.ORG:443/", scopes))
        self.assertFalse(is_allowed("https://foo.example.org/", scopes))
        self.assertFalse(is_allowed("https://example.org.evil.test/", scopes))
        self.assertFalse(is_allowed("https://evil.test/?next=example.org", scopes))

    def test_credentials_and_port_rejected(self):
        for url in ("https://name:pass@example.org/", "https://example.org:8443/",
                    "http://example.org/", "https://example.org/#fragment",
                    "https://127.0.0.1/", "https://localhost/"):
            self.assertIsNone(get_hostname(url), url)

    def test_file_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            scope = Path(directory) / "scope.txt"
            scope.write_text("# comment\nexample.org\n\n", encoding="utf-8")
            self.assertEqual(load_exact_hosts(scope), {"example.org"})
            scope.write_text("*.example.org\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_exact_hosts(scope)


if __name__ == "__main__":
    unittest.main()
