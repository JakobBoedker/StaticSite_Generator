from enum import Enum
import re

from htmlnode import LeafNode


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_image(old_nodes):
    final_list = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            final_list.append(node)
            continue
        current_text = node.text
        for link_alt, link_url in images:
            parts = current_text.split(f"![{link_alt}]({link_url})", 1)
            current_text = parts[-1]
            if parts[0]:
                final_list.append(TextNode(parts[0], TextType.NORMAL))
            final_list.append(TextNode(link_alt, TextType.IMAGE, link_url))
        if current_text:
            final_list.append(TextNode(current_text, TextType.NORMAL))
    return final_list


def split_nodes_link(old_nodes):
    final_list = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            final_list.append(node)
            continue
        current_text = node.text
        for link_text, link_url in links:
            parts = current_text.split(f"[{link_text}]({link_url})", 1)
            current_text = parts[-1]
            if parts[0]:
                final_list.append(TextNode(parts[0], TextType.NORMAL))
            final_list.append(TextNode(link_text, TextType.LINK, link_url))
        if current_text:
            final_list.append(TextNode(current_text, TextType.NORMAL))
    return final_list


def extract_markdown_images(text):
    find_alt = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return find_alt


def extract_markdown_links(text):
    find_link = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return find_link


def split_nodes_delimiter(old_nodes, delimiter, text_types):
    new_text_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_text_nodes.append(node)
            continue
        first_delimiter = node.text.find(delimiter)
        if first_delimiter == -1:
            new_text_nodes.append(node)
            continue
        second_delimiter = node.text.find(delimiter, first_delimiter + 1)
        if second_delimiter == -1:
            raise ValueError("No closing delimiter")
        new_text_nodes.append(TextNode(node.text[:first_delimiter], TextType.NORMAL))
        new_text_nodes.append(
            TextNode(
                node.text[first_delimiter + len(delimiter) : second_delimiter],
                text_types,
            )
        )
        new_text_nodes.append(
            TextNode(node.text[second_delimiter + len(delimiter) :], TextType.NORMAL)
        )
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
