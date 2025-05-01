# coins-parser

Parses and creates COinS metadata tags. Can be used with Zotero.

[![PyPI - Version](https://img.shields.io/pypi/v/coins-parser.svg)](https://pypi.org/project/coins-parser)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cff2toml.svg)](https://pypi.org/project/coins-parser)

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

```console
# parse a single COinS tag
from coins_parser import CoinsParser

html_with_coins_tags: str = ""

# print metadata for each COinS tag
coins = CoinsParser.parse(html_with_coins_tags)
for coin in coins:
    print(coin)
```

You can covert COinS objects back into HTML. 
This can be useful if you want to inject one or more COinS span tags into your webpage
so Zotero can recognize one or more items on a single page.

```
# Create two COinS objects
from coins_parser import CoinsParser

coin_1: list[tuple[str, str]] = [
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

coin_2: list[tuple[str, str]] = [
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
coins: list[list[tuple[str, str]]] = [coin_1, coin_2]
html: str = CoinsParser.html(coins)  
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