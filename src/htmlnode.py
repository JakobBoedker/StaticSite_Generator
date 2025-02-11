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
        if self.tag == None:
            return self.value
        return f"<{self.tag}{test}>{self.value}</{self.tag}>"
