class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        addedString = ""
        if self.props is None:
            return ""
        for item in self.props:
            addedString += " " + item + "=" + '"' + self.props[item] + '"'
        return addedString

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        test = self.props_to_html()
        if not self.value:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{test}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if not self.children:
            raise ValueError("Children is missing.")
        addedString = ""
        for item in self.children:
            addedString += item.to_html()
        return f"<{self.tag}>{addedString}</{self.tag}>"
