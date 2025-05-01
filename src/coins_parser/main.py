from bs4 import BeautifulSoup
from urllib.parse import parse_qsl, urlencode

CoinTerm = tuple[str, str]
Coin = list[CoinTerm]
CoinList = list[Coin]

COINS_HTML_ELEMENT: str = "span"
COINS_HTML_ELEMENT_ATTRIBUTE: str = "title"
COINS_HTML_ELEMENT_CLASS: str = "Z3988"


class CoinsParser:

    @staticmethod
    def parse(html: str, beautiful_soup_parser: str = None) -> CoinList:
        if beautiful_soup_parser is None:
            beautiful_soup_parser = "html.parser"
        soup = BeautifulSoup(html, beautiful_soup_parser)

        coins = []
        for coin_element in soup.find_all(
            COINS_HTML_ELEMENT, class_=COINS_HTML_ELEMENT_CLASS
        ):
            coin_element_attribute = coin_element.get(COINS_HTML_ELEMENT_ATTRIBUTE, "")
            coin = parse_qsl(coin_element_attribute)
            coins.append(coin)
        return coins

    @staticmethod
    def html(coins: CoinList) -> str:
        if not isinstance(coins, list):
            return ""
        html = ""
        for coin in coins:
            if isinstance(coin, list) and len(coin) > 0:
                html += f'<{COINS_HTML_ELEMENT} class="{COINS_HTML_ELEMENT_CLASS}" {COINS_HTML_ELEMENT_ATTRIBUTE}="{urlencode(coin)}"></{COINS_HTML_ELEMENT}>'
        return html

    if __name__ == "__main__":
        pass
