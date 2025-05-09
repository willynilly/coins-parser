# coins-parser

Parses and creates COinS metadata tags. Can be used with Zotero.

[![PyPI - Version](https://img.shields.io/pypi/v/coins-parser.svg)](https://pypi.org/project/coins-parser)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fwillynilly%2Fcoins-parser%2Fmain%2Fpyproject.toml)


---

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contribution](#contribution)

## Installation

```console
pip install coins-parser
```

## Usage


Zotero allows you to export references as COinS tags. You can use this package to parse them and use them in your Python packages. This package offers a CoinsParser class that can parse an HTML string containing COinS tags into a Python list. This list contains a list of COinS metadata for each COinS span tag found in the HTML string.

```python
# parse several COinS tags from an HTML string (it will ignore the other HTML elements)
from coins_parser import CoinsParser

html_with_coins_tags: str = """
<span class="Z3988" title="url_ver=Z39.88-2004&ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fzotero.org%3A2&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Adc&rft.type=computerProgram&rft.title=MyOtherApp&rft.publisher=Some+Other+Company&rft.description=This+is+another+example+dummy+software+for+testing.&rft.identifier=https%3A%2F%2Fzenodo.org%2Frecords%2Fsomenumber2&rft.aufirst=Willa&rft.aulast=Biley&rft.au=Willa+Biley&rft.au=Wil%C3%B2+Ril%C3%BC&rft.au=Jil+van+Hilo&rft.date=2025-04-20"></span>

<span class="Z3988" title="url_ver=Z39.88-2004&ctx_ver=Z39.88-2004&rfr_id=info%3Asid%2Fzotero.org%3A2&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Adc&rft.type=computerProgram&rft.title=MyOtherApp&rft.publisher=Some+Other+Company&rft.description=This+is+another+example+dummy+software+for+testing.&rft.identifier=https%3A%2F%2Fzenodo.org%2Frecords%2Fsomenumber2&rft.aufirst=Willa&rft.aulast=Biley&rft.au=Willa+Biley&rft.au=Wil%C3%B2+Ril%C3%BC&rft.au=Jil+van+Hilo&rft.date=2025-04-20"></span>
"""

# print metadata for each found COinS tag
coin_spans: CoinSpanList = CoinsParser.parse(html_with_coins_tags)
for coin_span in coin_spans:
    print(coin_span)
```

You can also specify the HTML parser used to [any parser supported by beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-a-parser). By default, the HTML parser is 'html.parser', which does not require installing additional packages. However, if you want to use a different HTML parser, like 'lxml', you will first need to install it as described in the previous link.

```python
### parse the COinS tags using the lxml parser
coin_spans: CoinSpanList = CoinsParser.parse(html_with_coins_tags, beautiful_soup_parser='lxml')
```

You can covert COinS objects back into HTML. 
This can be useful if you want to inject one or more COinS span tags into your webpage
so Zotero can recognize one or more items on a single page.

```python
# Create two COinS objects
from coins_parser import CoinsParser

coin_span_1: CoinSpan = [
    ("url_ver", "Z39.88-2004"),
    ("ctx_ver", "Z39.88-2004"),
    ("rfr_id", "info:sid/zotero.org:2"),
    ("rft_val_fmt", "info:ofi/fmt:kev:mtx:dc"),
    ("rft.type", "computerProgram"),
    ("rft.title", "MyApp"),
    ("rft.publisher", "Some Company"),
    ("rft.description", "This is an example dummy software for testing."),
    ("rft.identifier", "https://zenodo.org/records/somenumber1"),
    ("rft.aufirst", "Willa"),
    ("rft.aulast", "Biley"),
    ("rft.au", "Willa Biley"),
    ("rft.au", "Wilò Rilü"),
    ("rft.au", "Jil van Hilo"),
    ("rft.date", "2025-04-15"),
]

coin_span_2: CoinSpan = [
    ("url_ver", "Z39.88-2004"),
    ("ctx_ver", "Z39.88-2004"),
    ("rfr_id", "info:sid/zotero.org:2"),
    ("rft_val_fmt", "info:ofi/fmt:kev:mtx:dc"),
    ("rft.type", "computerProgram"),
    ("rft.title", "MyOtherApp"),
    ("rft.publisher", "Some Company"),
    ("rft.description", "This is another example dummy software for testing."),
    ("rft.identifier", "https://zenodo.org/records/somenumber2"),
    ("rft.aufirst", "Willa"),
    ("rft.aulast", "Biley"),
    ("rft.au", "Willa Biley"),
    ("rft.au", "Wilò Rilü"),
    ("rft.au", "Jil van Hilo"),
    ("rft.date", "2025-04-11"),
]
coin_spans: list[CoinSpan] = [coin_span_1, coin_span_2]
html: str = CoinsParser.html(coin_spans)  
print(html)
```


## License

`coins-parser` is distributed under the terms of the [Apache 2.0](https://spdx.org/licenses/Apache-2.0.html) license

## Contribution

Contributions in the form of feature requests, bug reports, bug fixes, tests, and feature implementations are welcome. To contribute code, please fork the project, and then do a pull request.

### Developer Notes

#### Building Locally

To build the tool locally, please follow the general advice from [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

```
python3 -m pip install --upgrade build
python3 -m build
```

#### Deploying

To deploy the tool, use the Github Action defined in .github/workflows/python-publish.yml