# beautifulsoup/apps/m3/task7.py
import os
import sys
import time

# Force Python to load your repository's version of bs4 instead of system-installed version
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from bs4 import BeautifulSoup
from bs4 import SoupReplacer

if len(sys.argv) < 2:
    print("Usage: python task7.py <path_to_html_file>")
    sys.exit(1)

input_file_path = sys.argv[1]

# decide parser type
parser = "html.parser" if input_file_path.endswith(".html") else "xml"

print(f"--- Milestone 3: Processing file for Task 7 using SoupReplacer API: {input_file_path} ---")

# Milestone 3: utilize attrs_xformer
def add_class_attr(tag):
    if tag.name == "p":
        # create a new class if I don't have one
        tag.attrs["class"] = "test"
    return tag.attrs

p_class_modifier = SoupReplacer(attrs_xformer=add_class_attr)

start_time = time.time()

try:
    with open(input_file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, parser, replacer=p_class_modifier)
except Exception as e:
    print(f"Error while parsing: {e}")
    sys.exit(1)

output_path = "output_m3_task7.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"Output written to {output_path}")
print(f"Completed in {time.time() - start_time:.4f} seconds.")
