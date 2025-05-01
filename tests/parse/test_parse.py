from tests.utils import run_parse_test
from coins_parser import CoinsParser


def test_parse_empty_string():
    html = ""
    assert CoinsParser.parse(html) == []


def test_parse_whitespace_string():
    html = "    "
    assert CoinsParser.parse(html) == []


def test_parse_html_with_single_non_coins_span():
    run_parse_test(test_name="single_non_coins_span")


def test_parse_html_with_single_empty_coins_span():
    run_parse_test(test_name="single_empty_coins_span")


def test_parse_html_with_multiple_empty_coins_spans():
    run_parse_test(test_name="multiple_empty_coins_spans")


def test_parse_html_with_single_non_empty_coins_span():
    run_parse_test(test_name="single_non_empty_coins_span")
