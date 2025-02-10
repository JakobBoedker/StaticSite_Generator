import unittest

from htmlnode import HTMLNode


class test_htmlnode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode(props={})
        return node.props_to_html() == ""


if __name__ == "__main__":
    unittest.main()
