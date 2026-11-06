"""Tests for tools/_guardrails.py. Run from the repo root:

    python3 -m unittest discover -s tests -v

No network access is needed: the parent class's request() is mocked, so these
tests only check what the guardrail lets through.
"""

import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

import requests  # noqa: E402
import _guardrails as g  # noqa: E402


class HttpGuardrailTest(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(requests.Session, "request", return_value="ok")
        self.parent_request = patcher.start()
        self.addCleanup(patcher.stop)
        self.http = g.session()

    def test_read_methods_pass_through(self):
        for verb in ("GET", "HEAD", "OPTIONS", "get"):
            self.assertEqual(self.http.request(verb, "https://api.example.com/items"), "ok")

    def test_helpers_are_guarded_too(self):
        self.assertEqual(self.http.get("https://api.example.com/items"), "ok")
        with self.assertRaises(g.ReadOnlyViolation):
            self.http.post("https://api.example.com/items", json={"a": 1})

    def test_write_methods_are_blocked_before_any_network_call(self):
        for verb in ("POST", "PUT", "PATCH", "DELETE"):
            with self.assertRaises(g.ReadOnlyViolation):
                self.http.request(verb, "https://api.example.com/items/1")
        self.parent_request.assert_not_called()

    def test_allowlisted_post_passes_only_for_that_endpoint(self):
        with mock.patch.object(g, "READ_ONLY_POST_ALLOWLIST", [("api.example.com", "/v1/search")]):
            self.assertEqual(self.http.post("https://api.example.com/v1/search"), "ok")
            with self.assertRaises(g.ReadOnlyViolation):
                self.http.post("https://api.example.com/v1/items")
            with self.assertRaises(g.ReadOnlyViolation):
                self.http.post("https://other.example.org/v1/search")


class SqlGuardrailTest(unittest.TestCase):
    def test_reads_pass(self):
        for q in (
            "SELECT * FROM leads WHERE id = 1;",
            "  select count(*) from tickets",
            "WITH recent AS (SELECT * FROM t) SELECT * FROM recent",
            "SHOW TABLES",
            "EXPLAIN SELECT 1",
            "SELECT note FROM t WHERE note = 'please update the record'",
            "SELECT 1 -- delete later",
            "SELECT REPLACE(name, 'a', 'b') FROM users",
        ):
            g.assert_read_only_sql(q)  # should not raise

    def test_writes_are_blocked(self):
        for q in (
            "DELETE FROM leads",
            "UPDATE leads SET stage = 'won'",
            "DROP TABLE leads",
            "SELECT 1; DROP TABLE leads",
            "WITH gone AS (DELETE FROM t RETURNING *) SELECT * FROM gone",
            "SELECT * INTO backup FROM leads",
            "",
        ):
            with self.assertRaises(g.ReadOnlyViolation, msg=q):
                g.assert_read_only_sql(q)


class AwsGuardrailTest(unittest.TestCase):
    def _hook(self):
        try:
            import boto3  # noqa: F401
        except ImportError:
            self.skipTest("boto3 not installed (only needed for AWS agents)")
        sess = g.readonly_boto3_session(region_name="us-east-1")
        client = sess.client("s3", aws_access_key_id="x", aws_secret_access_key="y")
        return client

    def test_write_operation_blocked_offline(self):
        client = self._hook()
        with self.assertRaises(g.ReadOnlyViolation):
            client.delete_bucket(Bucket="anything")


if __name__ == "__main__":
    unittest.main()
