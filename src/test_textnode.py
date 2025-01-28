# test 
import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is textnode", TextType.BOLD, "google.dk")
        node2 = TextNode("this is textnode", TextType.BOLD, "google.dk")
        self.assertEqual(node,node2)



if __name__ == "__main__":
    unittest.main()

