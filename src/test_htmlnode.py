import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
