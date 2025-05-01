from coins_parser import CoinsParser, CoinList
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
    coins: CoinList = CoinsParser.parse(input_html)
    assert json.dumps(coins, ensure_ascii=False) == expected_json


def run_html_test(test_name: str):
    test_group: str = "html"
    input_json: str = load_json(
        test_group=test_group, test_name=test_name, file_name="input.json"
    )
    expected_html: str = load_html(
        test_group=test_group, test_name=test_name, file_name="expected.html"
    )
    coins: CoinList = []
    for raw_coin_list in json.loads(input_json):
        coins.append([tuple(raw_coin_term) for raw_coin_term in raw_coin_list])
    print(coins)
    actual_html: str = CoinsParser.html(coins)
    assert actual_html == expected_html
