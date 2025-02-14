from enum import Enum

from htmlnode import LeafNode


def split_nodes_delimiter(old_nodes, delimiter, text_types):
    new_text_nodes = []
    delimiter_location = []
    before_delimiter = ""
    substring = ""
    after_delimiter = ""
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            new_text_nodes.append(node)
        for item in range(len(node.text)):
            if len(delimiter_location) == 0:
                before_delimiter += node.text[item]
            elif node.text[item] == delimiter and len(delimiter_location) == 0:
                delimiter_location.append(item)
                new_text_nodes.append(TextNode(before_delimiter, TextType.NORMAL))
            elif len(delimiter_location) == 1:
                substring += node.text[item]
            elif node.text[item] == delimiter and len(delimiter_location) != 0:
                delimiter_location.append(item)
                new_text_nodes.append(TextNode(substring, text_types))
            else:
                after_delimiter += node.text[item]
        new_text_nodes.append(TextNode(after_delimiter, TextType.NORMAL))
    return new_text_nodes


def text_node_to_html_node(textnode):
    if textnode.text_type == TextType.NORMAL:
        return LeafNode(None, textnode.text)
    if textnode.text_type == TextType.BOLD:
        return LeafNode("b", textnode.text)
    if textnode.text_type == TextType.ITALIC:
        return LeafNode("i", textnode.text)
    if textnode.text_type == TextType.CODE:
        return LeafNode("code", textnode.text)
    if textnode.text_type == TextType.LINK:
        return LeafNode("a", textnode.text, {"href": textnode.url})
    if textnode.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
