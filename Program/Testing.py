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


def test_valid_dual_segment_url():
    test_url = "https://example.com/track/aHR0cDovL2V4YW1wbGUuY29tL2ZpbGU/?auth=V2lsbGlhbVdhbGtlckBDcnV0Y2hmaWVsZC5jb20"
    print("\n--- Running: test_valid_dual_segment_url ---")
    SplitURL(test_url)

def test_url_with_noise_and_encoded_segment():
    test_url = "https://site.net?id=123&data=dGhpcyBpcyBhIHRlc3Qgc3RyaW5n==&extra=abc.def.ghi"
    print("\n--- Running: test_url_with_noise_and_encoded_segment ---")
    SplitURL(test_url)

def test_url_with_padding_stripped():
    test_url = "https://foo.com/u/c29tZXVzZXJAZXhhbXBsZS5jb20"  # "someuser@example.com"
    print("\n--- Running: test_url_with_padding_stripped ---")
    SplitURL(test_url)

def test_url_with_no_base64():
    test_url = "https://regularsite.com/profile/william-walker/metadata"
    print("\n--- Running: test_url_with_no_base64 ---")
    SplitURL(test_url)

def test_small_base64_segment():
    test_url = "https://x.com/data/c2ltcGxl"  # "simple"
    print("\n--- Running: test_small_base64_segment ---")
    SplitURL(test_url)

def test_broken_base64_segment():
    test_url = "https://x.com/id=SGVsbG8$RmF1bHQyQmFzZTY0=="  # contains invalid $
    print("\n--- Running: test_broken_base64_segment ---")
    SplitURL(test_url)

def test_url_with_encoded_email_and_path():
    test_url = "https://download.net/u/V2lsbGlhbUBXaG8uY29t/dmlkZW8="  # William@Who.com + "video"
    print("\n--- Running: test_url_with_encoded_email_and_path ---")
    SplitURL(test_url)

def test_url_with_mixed_encoding_styles():
    test_url = "https://toolbox/api/token/dG9rZW4tLS0_/ZGV0YWlscz9hPXJlcG9ydA=="  # 1 url-safe, 1 padded
    print("\n--- Running: test_url_with_mixed_encoding_styles ---")
    SplitURL(test_url)


def run_all_tests():
    test_valid_dual_segment_url()
    test_url_with_noise_and_encoded_segment()
    test_url_with_padding_stripped()
    test_url_with_no_base64()
    test_small_base64_segment()
    test_broken_base64_segment()
    test_url_with_encoded_email_and_path()
    test_url_with_mixed_encoding_styles()
    ExitMain()


if __name__ == "__main__":
    run_all_tests()
