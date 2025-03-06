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


def count_hash_in_heading(block):
    count = 0
    for item in block:
        if item == "#":
            count += 1
        if item == " ":
            break
    return f"h{count}"


def determind_block(block):
    typeOfBlock = block_to_block_type(block)
    if typeOfBlock == BlockType.PARAGRAPH:
        return HTMLNode("p", block)
    if typeOfBlock == BlockType.CODE:
        return HTMLNode("pre", HTMLNode("code", block.strip()))
    if typeOfBlock == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        list_of_li_nodes = []
        for line in lines:
            list_of_li_nodes.append(HTMLNode("li", line[2:]))
        return HTMLNode("ul", None, list_of_li_nodes)
    if typeOfBlock == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        list_of_li_nodes = []
        for line in lines:
            list_of_li_nodes.append(HTMLNode("li", line[3:]))
        return HTMLNode("ol", None, list_of_li_nodes)
    if typeOfBlock == BlockType.QUOTE:
        return HTMLNode("backquote", block[2:])
    if typeOfBlock == BlockType.HEADING:
        type_of_heading = count_hash_in_heading(block)
        if type_of_heading not in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            return HTMLNode("p", block)
        heading_content = block.lstrip("#").strip()
        return HTMLNode(type_of_heading, heading_content)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlblocks = []
    for block in blocks:
        htmlblocks.append(determind_block(block))
    return htmlblocks


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
