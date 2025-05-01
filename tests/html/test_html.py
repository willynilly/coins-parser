from tests.utils import run_html_test
from coins_parser import CoinsParser


def test_html_for_none_object():
    assert CoinsParser.html(None) == ""


def test_html_for_empty_array():
    assert CoinsParser.html([]) == ""


def test_html_for_no_coin_objects():
    assert CoinsParser.html([[]]) == ""


def test_html_single_coin_object():
    run_html_test(test_name="single_coin_object")


def test_html_multiple_coin_objects():
    run_html_test(test_name="multiple_coin_objects")
