# test
import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
