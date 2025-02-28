import textnode
import htmlnode


def main():
    node = textnode.TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) tes test test",
        textnode.TextType.NORMAL,
    )

    node1 = textnode.TextNode(
        "![to boot dev](https://www.boot.dev) This is text with a link",
        textnode.TextType.NORMAL,
    )
    new_nodes = textnode.split_nodes_link([node])
    print(new_nodes)


main()
