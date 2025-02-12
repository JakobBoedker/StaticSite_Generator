import textnode
import htmlnode


def main():
    dummydata = textnode.TextNode(
        "this is a text node", "italic", "https://www.boot.dev"
    )
    print(dummydata)

    test1 = htmlnode.LeafNode(
        "a", "This is some text.", props={"href": "https://www.google.com"}
    )
    print(test1.to_html())

    test2 = htmlnode.HTMLNode(props={"href": "https://www.google.com"})
    print(test2.props_to_html())

    node1 = htmlnode.ParentNode("p", [htmlnode.LeafNode("span", "Nested content")])

    print(node1.to_html())
    node = htmlnode.ParentNode(
        "section",
        [
            htmlnode.ParentNode(
                "article",
                [
                    htmlnode.ParentNode(
                        "header", [htmlnode.LeafNode(None, "This is a header!")]
                    ),
                    htmlnode.ParentNode(
                        "footer", [htmlnode.LeafNode(None, "This is a footer!")]
                    ),
                ],
            ),
            htmlnode.LeafNode("p", "Standalone paragraph"),
        ],
    )
    print(node.to_html())


main()
