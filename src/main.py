from markdown import *
from textnode import *
from htmlnode import *
from markdown import *


def main():
    md = """
``` 
code test 
```

> test


"""

    print(markdown_to_html_node(md))


main()
