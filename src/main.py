import textnode
import htmlnode


def main():
    node = textnode.TextNode("this is textnode", textnode.TextType.BOLD, "google.dk")
    print(textnode.text_node_to_html_node(node).to_html())


main()
