# Milestone-2

<details>
  <summary>
 <strong>Part 2: API Definition Locations<strong>
  </summary>

### 1. API names, located files and lines

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
 <strong>Part 3<strong>
  </summary>

| Changed File | Change Description | Purpose |
| :--- | :--- | :--- |
| **bs4/__init__.py** | Added "SoupReplacer" to __all__ | Expose SoupReplacer symbol from the package API so it can be imported via from bs4 import SoupReplacer |
| **bs4/__init__.py** | Added import: from .replacer import SoupReplacer and TYPE_CHECKING conditional import block | Import the SoupReplacer class into the package namespace; TYPE_CHECKING block helps type checkers without runtime import side-effects. |
| **bs4/__init__.py** | Added replacer | Allow users to pass a SoupReplacer instance to BeautifulSoup when constructing a soup. |
| **bs4/__init__.py** | Added assignment of the replacer | Store the replacer on the BeautifulSoup instance so parser/builders can access it during parsing. |
| **bs4/replacer.py** | Add new class SoupReplacer with constructor SoupReplacer(og_tag, alt_tag) and a method to check whether a tag should be replaced | Provides a way for users to define which HTML/XML tags should be replaced during parsing. |
| **bs4/builder/_htmlparser.py** | Added _map_name() method | Provides a single place to apply tag replacement logic. This makes parsing extensible without modifying core parser logic. |
| **bs4/builder/_htmlparser.py** | Inside _map_name(), used getattr(self.soup, "replacer", None) and invoked rp.maybe(name) | Allows BeautifulSoup to optionally replace tags only when a SoupReplacer is passed in, without affecting default parsing behavior. |
| **bs4/builder/_htmlparser.py** | Called name = self._map_name(name) inside: handle_startendtag(), handle_starttag(), and handle_endtag() | Ensures tag replacement happens during parsing, fulfilling Milestone-2 requirement that tree modification should occur before tree construction is finished. |

</details>
