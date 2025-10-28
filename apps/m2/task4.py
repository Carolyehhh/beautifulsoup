# task4_strainer.py - print all id attr tags using SoupStrainer

import sys
import time
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    print("Usage: python task4_strainer.py <path_to_html_file>")
    sys.exit(1)

input_file_path = sys.argv[1]
type = "html.parser" if input_file_path.endswith(".html") else "xml"

print(f"--- Processing file for Task 4 (Strainer): {input_file_path} ---")

# Set SoupStrainer: parse all tags that have an 'id' attribute
tags_with_id_attr = SoupStrainer(attrs={'id': True})

try:
    start_time = time.time()
    with open(input_file_path, 'r', encoding='utf-8') as f:
       
        soup = BeautifulSoup(f, type, parse_only=tags_with_id_attr)

except Exception as e:
    print(f"An error occurred during parsing: {e}")
    sys.exit(1)

def execute_task(soup: BeautifulSoup):
    tags_with_id = soup.find_all(id=True)

    if not tags_with_id:
        print("  No tags with 'id' attribute found (or none were parsed).")
        return

    for tag in tags_with_id:
        
        print(f"  <{tag.name} id='{tag.get('id')}'>...")

    end_time = time.time()
    print(f"\n[Task 4] Total tags with 'id' found: {len(tags_with_id)}")
    print(f"Parsing and execution completed in {end_time - start_time:.4f} seconds.")

if __name__ == '__main__':
    execute_task(soup)