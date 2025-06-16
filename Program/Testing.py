"""
Name:
    Testing
Author:
    William Walker @ Crutchfield
Description:
        testing grounds for bulk module testing instead of one by one in CLI
imports:
    @Base64URLSplitter.py
    @Exit.py
"""
from Base64URLSplitter import *
from Exit import *
from Redirect import *

import unittest
from unittest.mock import patch


class TestRedirectChainBuilder(unittest.TestCase):

    def setUp(self):
        GRAPH.clear()

    @patch('builtins.input', side_effect=["http://example.com", "http://redirect.com"])
    def test_new_redirect_chain(self, mock_input):
        NewRedirectChain()
        self.assertIn("hxxp://example[.]com", GRAPH)
        self.assertEqual(GRAPH["hxxp://example[.]com"], "hxxp://redirect[.]com")

    @patch('builtins.input', side_effect=[
        "http://example.com", "http://redirect.com",  # New chain
        "http://redirect.com", "http://final.com"     # Extend chain
    ])
    def test_extend_redirect_chain(self, mock_input):
        NewRedirectChain()
        ExtendRedirectChain()
        self.assertEqual(GRAPH["hxxp://redirect[.]com"], "hxxp://final[.]com")
        chain = trace_redirect_chain("hxxp://example[.]com")
        self.assertIn("hxxp://final[.]com", chain)

    def test_trace_redirect_chain(self):
        GRAPH["hxxp://a[.]com"] = "hxxp://b[.]com"
        GRAPH["hxxp://b[.]com"] = "hxxp://c[.]com"
        chain = trace_redirect_chain("hxxp://a[.]com")
        expected = "\n    ------Redirect----->\n    ".join([
            "hxxp://a[.]com", "hxxp://b[.]com", "hxxp://c[.]com"
        ])
        self.assertEqual(chain, expected)

    @patch('builtins.input', side_effect=["hxxp://example[.]com", "hxxp://redirect[.]com"])
    def test_already_sanitized_input(self, mock_input):
        NewRedirectChain()
        self.assertIn("hxxp://example[.]com", GRAPH)
        self.assertEqual(GRAPH["hxxp://example[.]com"], "hxxp://redirect[.]com")



    def test_long_redirect_chain(self):
        urls = [f"hxxp://site{i}[.]com" for i in range(5)]
        for i in range(len(urls) - 1):
            GRAPH[urls[i]] = urls[i + 1]
        chain = trace_redirect_chain(urls[0])
        for url in urls:
            self.assertIn(url, chain)

    @patch('builtins.input', side_effect=["http://nonexistent.com", "http://newtarget.com"])
    def test_extend_nonexistent_tail(self, mock_input):
        ExtendRedirectChain()
        # The graph should remain empty because the base URL doesn't exist
        self.assertNotIn("hxxp://nonexistent[.]com", GRAPH)
        self.assertEqual(len(GRAPH), 0)


if __name__ == '__main__':
    unittest.main()

