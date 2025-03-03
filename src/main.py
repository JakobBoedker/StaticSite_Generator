from markdown import *
from textnode import *
from htmlnode import *
from markdown import *


def main():
    md = """
###### test

> test


1. test


```code test```


This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    test = markdown_to_blocks(md)
    newlist = []
    for block in test:
        newlist.append(block_to_block_type(block))

    print(newlist)


main()
