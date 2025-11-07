# Milestone 3 - SoupReplacer API Enhancement

## 1. Project Overview
In Milestone 3, I extended the `SoupReplacer` class to provide a more flexible and powerful interface for transforming HTML tags and text nodes during parsing. Unlike Milestone 2, which only supported simple tag replacement (`og_tag` → `alt_tag`), Milestone 3 introduces three transformer functions that allow more advanced modifications.


## 2. API Comparison: Milestone 2 vs Milestone 3

| Feature | Milestone 2 | Milestone 3 |
|---------|------------|------------|
| Replace tag name | `og_tag` → `alt_tag` | `name_xformer` (function to compute new tag name; receives each Tag object; can handle lowercase/uppercase) |
| Modify attributes | Not supported | `attrs_xformer` (function returning new attribute dictionary) |
| Modify tag or text content | Not supported | `xformer` (function with side effects; can mutate `Tag` or `NavigableString`) |
| Recursive transformations | Not supported | Applies to all children including text nodes |


## 3. Design Considerations / Recommendations
- Milestone 3 API is more general and extensible.
- Supports operations on both tag nodes and text nodes (NavigableString).
- `xformer` allows side-effects on tags and text, which can cover a wide range of HTML transformations.
- For future enhancements of BeautifulSoup, this API provides a clean hook for user-defined transformations.

## 4. Usage Examples

#### a. name_xformer
```python
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

html_doc = "<b>bold text</b>"

# Build a SoupReplacer with a name_xformer function.
# This function will be called on each Tag during apply_replacer.
# It should return the new tag name (or the original if no change).
replacer = SoupReplacer(
    name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
)

# Build a BeautifulSoup object
soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

# Apply the replacer to the entire tree
# This will recursively transform all tags using name_xformer
replacer.apply_replacer(soup)

print(soup.prettify())
```

#### b. attrs_xformer
```python
# Define a function that returns new attributes for a tag
def add_title(tag):
    if tag.name == "p":
        # Return a new dict that will replace the original tag.attrs
        return {"title": "paragraph"}
    # If no change, return the original attributes
    return tag.attrs

# Build a SoupReplacer using attrs_xformer
attr_replacer = SoupReplacer(attrs_xformer=add_title)

# Apply the replacer
attr_replacer.apply_replacer(soup)
```


#### c. xformer
```python
# Define a function that modifies a tag or text in place
def remove_class_attr(tag):
    # xformer can mutate the tag directly
    if "class" in tag.attrs:
        del tag.attrs["class"]

# Build a SoupReplacer using xformer
class_deleter = SoupReplacer(xformer=remove_class_attr)

# Apply the replacer
class_deleter.apply_replacer(soup)
```


#### d. Task7 Example
Task7 now uses the Milestone 3 API to transform tags and text dynamically. (See task7.py)

## 5. Testing
* Test cases located in <span style="color:yellow;">beautifulsoup/bs4/tests/test_milestone3.py</span>
* To run the tests, execute:

```bash
pytest beautifulsoup/bs4/tests/test_milestone3.py -v
```
* 6 test cases implemented and all passed successfully.

## 6. Task7 Application Testing

* The application program located in <span style="color:yellow;">beautifulsoup/apps/m3/task7.py</span> demonstrates the Milestone 3 API in practice.
* To run the application, execute:

```bash
python beautifulsoup/apps/m3/task7.py <path_to_html_file>
```

* outcome: output_m3_task7.html