from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"


class TextNode():
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.url = URL
        self.text_type = TextType(TEXT_TYPE)
    

    def __eg__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

