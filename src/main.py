import textnode
import htmlnode


def main():
    node = textnode.TextNode(
        "This is text with a `code block` word", textnode.TextType.NORMAL
    )
    new_nodes = textnode.split_nodes_delimiter([node], "`", textnode.TextType.CODE)
    print(new_nodes)


main()
