# Milestone 4: Iterable BeautifulSoup

## Overview
This milestone introduces the ability to iterate over a `BeautifulSoup` object (and any `Tag` object) directly using a `for` loop. The iteration performs a **Depth-First Search (DFS)** traversal over the entire parse tree.

## Implementation Details
The implementation modifies the `PageElement` class in `bs4/element.py`.

### Key Features:
1.  **Generator-based Iteration**: 
    Instead of collecting all nodes into a list (which would consume significant memory for large trees), we implemented the `__iter__` method as a Python **generator** using the `yield` keyword.
    
2.  **Depth-First Search (DFS)**:
    The iteration logic starts at the current node and recursively visits all children.
    - It yields the current node (`self`).
    - It iterates through `self.contents`.
    - If a child is a `Tag`, it recursively yields from that child (`yield from child`).
    - If a child is a `NavigableString` (leaf node), it yields the child directly.

### Example Usage:
```python
soup = BeautifulSoup(html_doc, 'html.parser')
for node in soup:
    print(node)
```

### Testing:
5 unit tests were added in `bs4/tests/test_m4.py` covering:
- Simple iteration
- DFS order verification
- Generator type verification
- Deeply nested trees
- Mixed content (Tags and Strings)