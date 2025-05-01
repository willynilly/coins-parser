from coins_parser import CoinsParser, CoinList
from pathlib import Path
import json


def load_input_html(test_group: str, test_name: str) -> str:
    return Path("tests", test_group, test_name, "input.html").read_text(
        encoding="UTF-8"
    )


def load_expected_output_json(test_group, test_name: str) -> str:
    return json.dumps(
        json.loads(
            Path("tests", test_group, test_name, "expected_output.json").read_text(
                encoding="UTF-8"
            )
        ),
        ensure_ascii=False,
    )


def run_test(test_group: str, test_name: str):
    html: str = load_input_html(test_group=test_group, test_name=test_name)
    expected_json: str = load_expected_output_json(
        test_group=test_group, test_name=test_name
    )
    coins: CoinList = CoinsParser.parse(html)
    assert json.dumps(coins, ensure_ascii=False) == expected_json
