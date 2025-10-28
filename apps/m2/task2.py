# task2_strainer.py - print <a> tags using SoupStrainer

import sys
import time
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    print("Usage: python task2_strainer.py <path_to_html_file>")
    sys.exit(1)

input_file_path = sys.argv[1]
type = "html.parser" if input_file_path.endswith(".html") else "xml"

print(f"--- Processing file for Task 2 (Strainer): {input_file_path} ---")

# Set SoupStrainer: parse only <a> tags
only_a_tags = SoupStrainer('a')

try:
    start_time = time.time()
    with open(input_file_path, 'r', encoding='utf-8') as f:
        # 將 SoupStrainer 作為 parse_only 參數傳入
        soup = BeautifulSoup(f, type, parse_only=only_a_tags)

except Exception as e:
    print(f"An error occurred during parsing: {e}")
    sys.exit(1)

def execute_task(soup: BeautifulSoup):
    # only parsed <a> tags, get data directly from soup.contents
    hyperlinks = soup.find_all('a')
    total_links = len(hyperlinks)

    if not hyperlinks:
        print("  No <a> tags found in the document (or none were parsed).")
    else:
        for link in hyperlinks:
            href = link.get('href')
            text = link.get_text(strip=True)
            print(f"  Href: {href}, Text: {text}")

    end_time = time.time()
    print(f"\n[Task 2] Total hyperlinks found: {total_links}")
    print(f"Parsing and execution completed in {end_time - start_time:.4f} seconds.")

if __name__ == '__main__':
    execute_task(soup)