import unittest

from htmlnode import HTMLNode, LeafNode
import htmlnode


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


class test_leadnode(unittest.TestCase):
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


class test_parentnode(unittest.TestCase):
    def test_one_child(self):
        node = htmlnode.ParentNode("a", [htmlnode.LeafNode("span", "Nested content")])
        nodestr = str(node.to_html())
        self.assertEqual(nodestr, "<a><span>Nested content</span></a>")

    def test_no_child(self):
        node = htmlnode.ParentNode("a", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_none_tag(self):
        node = htmlnode.ParentNode(None, [htmlnode.LeafNode("span", "Nested content")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_deep_children(self):
        node = htmlnode.ParentNode(
            "section",
            [
                htmlnode.ParentNode(
                    "article",
                    [
                        htmlnode.ParentNode(
                            "header", [htmlnode.LeafNode(None, "This is a header!")]
                        ),
                        htmlnode.ParentNode(
                            "footer", [htmlnode.LeafNode(None, "This is a footer!")]
                        ),
                    ],
                ),
                htmlnode.LeafNode("p", "Standalone paragraph"),
            ],
        )
        nodestr = str(node.to_html())
        self.assertEqual(
            nodestr,
            "<section><article><header>This is a header!</header><footer>This is a footer!</footer></article><p>Standalone paragraph</p></section>",
        )


if __name__ == "__main__":
    unittest.main()
