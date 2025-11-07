# beautifulsoup/bs4/tests/test_milestone3.py
import pytest
from bs4 import BeautifulSoup, NavigableString
from bs4.replacer import SoupReplacer

HTML_DOC = """
<html><body>
  <p id="p1" class="foo">This is a <b>bold</b> and <i class="x">italic</i> text.</p>
  <div><B>Upper B</B></div>
  <span class="keep" data-x="1">span</span>
</body></html>
"""

def test_name_xformer_changes_b_to_blockquote():
    replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name.lower() == "b" else tag.name)
    soup = BeautifulSoup(HTML_DOC, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None
    assert "bold" in soup.blockquote.text or "Upper B" in soup.blockquote.text

def test_og_tag_alt_tag_backwards_compatibility():
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(HTML_DOC, "html.parser", replacer=replacer)
    assert len(soup.find_all("blockquote")) >= 1

def test_attrs_xformer_removes_class():
    def remove_class(tag):
        if "class" in tag.attrs:
            d = dict(tag.attrs)
            d.pop("class", None)
            return d
        return tag.attrs
    replacer = SoupReplacer(attrs_xformer=remove_class)
    soup = BeautifulSoup(HTML_DOC, "html.parser", replacer=replacer)
    # no tag should have 'class' attribute that originally had it
    assert not any("class" in t.attrs for t in soup.find_all(True) if t.name in ("p","i"))

def test_xformer_can_mutate_tag_contents():
    def uppercase_text(tag):
        # uppercase direct string children (safe minimal example)
        if isinstance(tag, NavigableString):
            tag.replace_with(tag.upper())

    replacer = SoupReplacer(xformer=uppercase_text)
    soup = BeautifulSoup("<p>hello</p>", "html.parser")
    replacer.apply_replacer(soup) # multually apply apply_replacer
    assert "HELLO" in str(soup)

def test_combined_name_and_attrs_transformer():
    def rm_class(tag):
        if "class" in tag.attrs:
            tag.attrs.pop("class", None)
            return tag.attrs
        return tag.attrs
    replacer = SoupReplacer(
        name_xformer=lambda tag: "section" if tag.name == "div" else tag.name,
        attrs_xformer=rm_class,
    )
    soup = BeautifulSoup("<div class='a'>x</div>", "html.parser", replacer=replacer)
    # name changed and class removed
    assert soup.find("section") is not None
    assert "class" not in soup.find("section").attrs

def test_no_replacer_does_not_change_tree():
    soup = BeautifulSoup("<b>ok</b><p>p</p>", "html.parser")
    assert soup.find("b") is not None
    assert soup.find("p") is not None
