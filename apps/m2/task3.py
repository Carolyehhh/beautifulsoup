# task3_strainer.py - print all tags using SoupStrainer

import sys
import time
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    print("Usage: python task3_strainer.py <path_to_html_file>")
    sys.exit(1)

input_file_path = sys.argv[1]
type = "html.parser" if input_file_path.endswith(".html") else "xml"

print(f"--- Processing file for Task 3 (Strainer): {input_file_path} ---")

# Set SoupStrainer: parse all tags (by passing True)
all_tags = SoupStrainer(True)

try:
    start_time = time.time()
    with open(input_file_path, 'r', encoding='utf-8') as f:
        # parse_only is the only parameter of SoupStrainer
        soup = BeautifulSoup(f, type, parse_only=all_tags)

except Exception as e:
    print(f"An error occurred during parsing: {e}")
    sys.exit(1)

def execute_task(soup: BeautifulSoup):
    # same logic with m1 task3
    all_tags = soup.find_all(True)

    counter = 1
    for tag in all_tags:
        attributes = ""
        if 'id' in tag.attrs:
            attributes += f" id='{tag.get('id')}'"
        if 'class' in tag.attrs:
            # 處理 class 列表
            attributes += f" class='{tag.get('class')[0]}...'"

        print(f"  {counter}. <{tag.name}{attributes}>")
        counter += 1

    end_time = time.time()
    print(f"\n[Task 3] Total tags found: {len(all_tags)}")
    print(f"Parsing and execution completed in {end_time - start_time:.4f} seconds.")

if __name__ == '__main__':
    execute_task(soup)