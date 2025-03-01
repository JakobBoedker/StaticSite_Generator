import textnode
import htmlnode


def main():
    node = textnode.TextNode(
        "This is **text** with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) tes test test",
        textnode.TextType.NORMAL,
    )

    node1 = textnode.TextNode(
        "![to boot dev](https://www.boot.dev) This is text with a link",
        textnode.TextType.NORMAL,
    )
    node2 = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    newnodes = textnode.text_to_textnodes(node2)
    print(newnodes)


main()
