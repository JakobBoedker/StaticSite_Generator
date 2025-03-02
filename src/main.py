from markdown import markdown_to_blocks
from textnode import *
from htmlnode import *
from markdown import *


def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
    test = markdown_to_blocks(md)
    print(test)


main()
