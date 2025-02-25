import textnode
import htmlnode


def main():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(textnode.extract_markdown_links(text))


main()
