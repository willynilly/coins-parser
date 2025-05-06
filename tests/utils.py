from coins_parser import CoinsParser, CoinSpanList, CoinSpanTerm
from pathlib import Path
import json


def load_html(test_group: str, test_name: str, file_name: str) -> str:
    return Path("tests", test_group, test_name, file_name).read_text(encoding="UTF-8")


def load_json(test_group, test_name: str, file_name: str) -> str:
    return json.dumps(
        json.loads(
            Path("tests", test_group, test_name, file_name).read_text(encoding="UTF-8")
        ),
        ensure_ascii=False,
    )


def run_parse_test(test_name: str):
    test_group: str = "parse"
    input_html: str = load_html(
        test_group=test_group, test_name=test_name, file_name="input.html"
    )
    expected_json: str = load_json(
        test_group=test_group, test_name=test_name, file_name="expected.json"
    )
    coin_spans: CoinSpanList = CoinsParser.parse(input_html)
    assert json.dumps(coin_spans, ensure_ascii=False) == expected_json


def run_html_test(test_name: str):
    test_group: str = "html"
    input_json: str = load_json(
        test_group=test_group, test_name=test_name, file_name="input.json"
    )
    expected_html: str = load_html(
        test_group=test_group, test_name=test_name, file_name="expected.html"
    )
    coin_spans: CoinSpanList = []
    for raw_coin_span_list in json.loads(input_json):
        coin_spans.append(
            [tuple(raw_coin_span_term) for raw_coin_span_term in raw_coin_span_list]
        )
    actual_html: str = CoinsParser.html(coin_spans)
    assert actual_html == expected_html
