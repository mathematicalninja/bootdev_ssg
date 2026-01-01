from src.tagTypes import HTML_TAG
from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    pass

    def __init__(
        self,
        value: str,
        tag: HTML_TAG | None,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag=tag, value=value, props=props)
        pass

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("all leaves must have values")
        if self.tag is None:
            return self.value
        if self.tag == "COMMENT":
            left = "<!--"
            right = "-->"
        return super().to_html()
