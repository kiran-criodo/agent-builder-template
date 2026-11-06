"""Offline tests for repo_snapshot.py. Run from the repo root:

    python3 -m unittest discover -s examples/repo-snapshot -v
"""

import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import repo_snapshot as rs  # noqa: E402

TODAY = dt.date(2026, 11, 6)

SAMPLE = {
    "full_name": "octo/hello",
    "description": "A friendly repo",
    "stargazers_count": 42,
    "forks_count": 7,
    "open_issues_count": 3,
    "language": "Python",
    "license": {"spdx_id": "MIT"},
    "topics": ["ai-agents", "template"],
    "is_template": True,
    "pushed_at": "2026-10-30T12:00:00Z",
    "html_url": "https://github.com/octo/hello",
}


class ParseRepoTest(unittest.TestCase):
    def test_accepts_slug_and_urls(self):
        for text in ("octo/hello", "https://github.com/octo/hello", "github.com/octo/hello.git/"):
            self.assertEqual(rs.parse_repo(text), "octo/hello")

    def test_rejects_garbage(self):
        with self.assertRaises(ValueError):
            rs.parse_repo("not a repo")


class SummariseTest(unittest.TestCase):
    def test_contains_the_facts_from_the_api(self):
        md = rs.summarise(SAMPLE, TODAY)
        self.assertIn("# Snapshot: octo/hello", md)
        self.assertIn("| Stars | 42 |", md)
        self.assertIn("| Licence | MIT |", md)
        self.assertIn("ai-agents, template", md)
        self.assertIn("active (last push 7 days ago)", md)
        self.assertNotIn("no licence file", md)

    def test_flags_missing_licence_and_description(self):
        repo = dict(SAMPLE, license=None, description=None, topics=[])
        md = rs.summarise(repo, TODAY)
        self.assertIn("_No description set._", md)
        self.assertIn("| Licence | none |", md)
        self.assertIn("no licence file", md)

    def test_activity_buckets(self):
        self.assertTrue(rs.activity_label("2026-08-01T00:00:00Z", TODAY).startswith("quiet"))
        self.assertTrue(rs.activity_label("2025-01-01T00:00:00Z", TODAY).startswith("dormant"))


if __name__ == "__main__":
    unittest.main()
