from htmlnode import *
from textnode import *


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
