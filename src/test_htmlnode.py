import unittest

from htmlnode import HTMLNode, LeafNode


class test_htmlnode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode(props={})
        return node.props_to_html() == ""

    def test_propt_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        strnode = str(node.props_to_html())
        self.assertEqual(strnode, ' href="https://www.google.com" target="_blank"')

    def test_all_props(self):
        node = HTMLNode()
        return node == ""

    def test_leafNode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        return node

    def test_leafNode_against_string(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        nodestr = str(node.to_html())
        self.assertEqual(nodestr, '<a href="https://www.google.com">Click me!</a>')

    def test_all_members(self):
        node = LeafNode(None, "This is text")
        return node


if __name__ == "__main__":
    unittest.main()
