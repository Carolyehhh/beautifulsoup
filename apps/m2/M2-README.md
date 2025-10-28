# Milestone-2

<details>
  <summary>
 Part 2: API Definition Locations
  </summary>

## 1. API names, located files and lines

| API name | File name | Line |
| :--- | :--- | :--- |
| **BeautifulSoup** | `./bs4/__init__.py` | 133 |
| **BeautifulSoup** | `./bs4/builder/_htmlparser.py` | 61 |
| **BeautifulSoup** | `./bs4/builder/_html5lib.py` | 323 |
| **SoupStrainer** | `./bs4/filter.py` | 313 |
| **find_parent** | `./bs4/element.py` | 992 |
| **find_next_sibling** | `./bs4/element.py` | 803 |
| **prettify** | `./bs4/element.py` | 2601 |
| **get** | `./bs4/element.py` | 2160 |
| **get_text** | `./bs4/element.py` | 524 |
| **find_all** | `./bs4/element.py` | 2715 |
| **find_all** | `./bs4/filter.py` | 137 |

</details>


<details>
  <summary>
 Part 3
  </summary>

| Changed File | Details |
| :--- | :--- |
| **bs4/soupreplacer.py** | new class |
| **bs4/__init__.py** | + `self.replacer = kwargs.pop("replacer", None)` |
| **bs4/builder/_htmlparser.py** | method **handle_starttag** + `if self.soup.replacer: name = self.soup.replacer.replace(name)` |
| **tests/test_soupreplacer.py** | new test file |

</details>
