from typing import Optional
from bs4 import BeautifulSoup, Tag
from urllib.parse import parse_qsl, urlencode

CoinSpanTerm = tuple[str, str]
CoinSpan = list[CoinSpanTerm]
CoinSpanList = list[CoinSpan]

COINS_HTML_ELEMENT: str = "span"
COINS_HTML_ELEMENT_ATTRIBUTE: str = "title"
COINS_HTML_ELEMENT_CLASS: str = "Z3988"


class CoinsParser:

    @staticmethod
    def parse(html: str, beautiful_soup_parser: Optional[str] = None) -> CoinSpanList:
        if beautiful_soup_parser is None:
            beautiful_soup_parser = "html.parser"
        soup = BeautifulSoup(html, beautiful_soup_parser)

        coin_spans = []
        for coins_html_element in soup.find_all(
            COINS_HTML_ELEMENT, class_=COINS_HTML_ELEMENT_CLASS
        ):
            if isinstance(coins_html_element, Tag):
                coins_html_element_attribute = coins_html_element.get(
                    COINS_HTML_ELEMENT_ATTRIBUTE, ""
                )
                coin_span: CoinSpan = parse_qsl(str(coins_html_element_attribute))
                coin_spans.append(coin_span)
        return coin_spans

    @staticmethod
    def html(coin_spans: CoinSpanList) -> str:
        if not isinstance(coin_spans, list):
            return ""
        html = ""
        for coin_span in coin_spans:
            if isinstance(coin_span, list) and len(coin_span) > 0:
                html += f'<{COINS_HTML_ELEMENT} class="{COINS_HTML_ELEMENT_CLASS}" {COINS_HTML_ELEMENT_ATTRIBUTE}="{urlencode(coin_span)}"></{COINS_HTML_ELEMENT}>'
        return html

    if __name__ == "__main__":
        pass
