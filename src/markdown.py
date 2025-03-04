from enum import Enum
from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import (
    text_node_to_html_node,
    text_to_textnodes,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
    TextType,
    TextNode,
)


def determind_block(block):
    if block == BlockType.PARAGRAPH:
        return LeafNode("p", block)
    if block == BlockType.HEADING:
        pass


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        which_block = block_to_block_type(block)


def markdown_to_blocks(markdown):
    if markdown:
        final_list = []
        splited_to_blocks = markdown.split("\n\n")
        for item in splited_to_blocks:
            stripedItem = item.strip()
            if stripedItem:
                final_list.append(stripedItem)
    else:
        raise Exception("Document Empty")
    return final_list


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
