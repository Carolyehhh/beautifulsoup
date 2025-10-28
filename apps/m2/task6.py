# task6_replacer.py 

import sys
import time
from bs4 import BeautifulSoup, Tag
# import SoupReplacer from self-defined bs4.replacer module
from bs4.soupreplacer import SoupReplacer 

TEST_HTML_DOC = """
<html>
<head><title>SoupReplacer Testing</title></head>
<body>
  <h1>Test Topic</h1>
  <p id="p1">This is a <b>粗體</b> declaration.</p>
  <div>another <B>upper letter</B> declaration</div>
  <a href="#">Unaffected links</a>
  <B>The third B tags</B>
</body>
</html>
"""

def run_task_and_tests(html_content: str):
    """
    Task 6: replace <b>/B with <blockquote>。
    """
    
    # b/B -> blockquote
    b_to_blockquote = SoupReplacer("b", "blockquote")
    
    print("--- Implement SoupReplacer task (b/B -> blockquote) ---")
    
    start_time = time.time()
    
    # 2. deliver replacer param
    soup = BeautifulSoup(html_content, 'html.parser', replacer=b_to_blockquote) 
    
    end_time = time.time()

    # --- Test Case 1: function verification ---
    # Check if original <b> and <B> tags been replaced as <blockquote>
    expected_replacements = 3 # 1 <b> + 2 <B> = 3 replacement
    replaced_blockquote_tags = soup.find_all('blockquote')
    
    # --- Test Case 2---
    # Check if the number of <p> tag still = 1
    p_tags = soup.find_all('p')
    a_tags = soup.find_all('a')
    
    print(f"complete in {end_time - start_time:.4f} seconds")
    print("---------------------------------------------------------")
    print(f"[Test 1] get the number of <blockquote> (expected: {expected_replacements}): {len(replaced_blockquote_tags)}")
    print(f"[Test 2] stay <p> quantity remain: {len(p_tags)}")
    print(f"[Test 2] stay <a> quantity remain: {len(a_tags)}")

    output_path = "output_task6_replaced.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    print(f"Reviesed document: {output_path}")

    print("\n--- After replacing HTML clips(Task 6 verufication) ---")
    print(soup.prettify())


if __name__ == '__main__':
    run_task_and_tests(TEST_HTML_DOC)