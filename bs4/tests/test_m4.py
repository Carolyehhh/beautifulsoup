import unittest
from bs4 import BeautifulSoup, Tag, NavigableString

class TestIterableSoup(unittest.TestCase):
    
    # Test 1: single node
    # Expected order: Soup -> <html> -> <body> -> <p> -> "Hello"
    def test_simple_iteration(self):
        html = "<p>Hello</p>"
        soup = BeautifulSoup(html, 'html.parser')
        
        # Collect all iterated nodes
        nodes = [node for node in soup]
        
        # verify volumns (Soup itself + html + body + p + text = 5 items)
        # causion: html.parser usually adds html and body tag automatically
        self.assertGreater(len(nodes), 1)
        
        # Verify the first node = Soup itself
        self.assertIsInstance(nodes[0], BeautifulSoup)
        # Verify the last node is text "Hello"
        self.assertIsInstance(nodes[-1], NavigableString)
        self.assertEqual(nodes[-1], "Hello")

    # Test2: Verify DFS
    # Structure:
    # <div>
    #   <a>TextA</a>
    #   <b>TextB</b>
    # </div>
    # Expected Order: div -> a -> TextA -> b -> TextB
    def test_dfs_order(self):
        html = "<div><a>TextA</a><b>TextB</b></div>"
        soup = BeautifulSoup(html, 'html.parser')
        
        # To simplify, I only check the iterater in div
        div_tag = soup.find('div')
        nodes = [node for node in div_tag]
        
        # Order should be:
        # 0: div (self)
        # 1: a
        # 2: TextA
        # 3: b
        # 4: TextB
        
        self.assertEqual(nodes[0].name, 'div')
        self.assertEqual(nodes[1].name, 'a')
        self.assertEqual(nodes[2], 'TextA')
        self.assertEqual(nodes[3].name, 'b')
        self.assertEqual(nodes[4], 'TextB')

    # Test3: Verify object type(make sure is Generator)
    # "should not collect the nodes ... onto a list"
    def test_is_generator(self):
        html = "<p>test</p>"
        soup = BeautifulSoup(html, 'html.parser')
        
        # gain iterator
        iterator = iter(soup)
        
        # Verify it is a iterator/generator instead of a list
        self.assertTrue(hasattr(iterator, '__next__'))
        self.assertFalse(isinstance(iterator, list))

    # Test 4: Deeply Nested
    # <div><p><span>Deep</span></p></div>
    def test_nested_structure(self):
        html = "<div><p><span>Deep</span></p></div>"
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div')
        
        names = []
        for node in div:
            if isinstance(node, Tag):
                names.append(node.name)
            elif isinstance(node, NavigableString):
                names.append(node.string)
                
        # Expected Order: div, p, span, Deep
        expected = ['div', 'p', 'span', 'Deep']
        self.assertEqual(names, expected)

    # Test 5: Mixed (Sibling nodes)
    # <root>Text1<br>Text2</root>
    def test_mixed_siblings(self):
        html = "<div>Text1<br>Text2</div>"
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div')
        
        nodes = list(div)
        
        # 0: div
        # 1: Text1
        # 2: br
        # 3: Text2
        self.assertEqual(nodes[1], "Text1")
        self.assertEqual(nodes[2].name, "br")
        self.assertEqual(nodes[3], "Text2")

if __name__ == '__main__':
    unittest.main()