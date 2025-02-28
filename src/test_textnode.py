# test
import unittest

from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is textnode", TextType.BOLD, "google.dk")
        node2 = TextNode("this is textnode", TextType.BOLD, "google.dk")
        self.assertEqual(str(node), str(node2))

    def test_not_eq(self):
        node1 = TextNode("this is textnode 1", TextType.ITALIC, "dinmor.dk")
        node3 = TextNode("this is textnode 3", TextType.BOLD, "google.dk")
        self.assertNotEqual(node1, node3)

    def test_is_none(self):
        node1 = TextNode("this is textnode 1", TextType.ITALIC, None)
        return node1


class TestTextToHTML(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is textnode", TextType.BOLD, "google.dk")
        nodestr = text_node_to_html_node(node).to_html()
        self.assertEqual(nodestr, "<b>this is textnode</b>")


class TestSplitByDelimiter(unittest.TestCase):
    pass


class TestLinkExtrations(unittest.TestCase):
    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = extract_markdown_images(text)
        self.assertEqual(
            node,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = extract_markdown_links(text)
        self.assertEqual(
            node,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )


class TestLinkAndImageSpliter(unittest.TestCase):
    def test_link_split(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) tes test test",
            TextType.NORMAL,
        )
        nodestr = str(
            split_nodes_link([node]),
        )
        self.assertNotEqual(
            nodestr,
            "[TextNode(This is text with a link , normal, None), TextNode(to boot dev, link, https://www.boot.dev), TextNode( and , normal, None), TextNode(to youtube, link, https://www.youtube.com/@bootdotdev), TextNode( tes test test, normal, None)]",
        )


if __name__ == "__main__":
    unittest.main()
