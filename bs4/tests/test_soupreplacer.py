from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

def test_replace_b_to_blockquote():
    html = "<html><body><b>text</b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("b") is None
    assert soup.find("blockquote").text == "text"

def test_non_matching_tag_no_change():
    html = "<html><body><i>text</i></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("i") is not None
