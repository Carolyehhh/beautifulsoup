# beautifulsoup/apps/m4/task8.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
</body></html>
"""

print("--- Testing Iterable Soup in Client Space ---")
soup = BeautifulSoup(html_doc, 'html.parser')

# Client Space Code
for node in soup:
    print(f"Node: {type(node).__name__} -> {str(node)[:30]}...")