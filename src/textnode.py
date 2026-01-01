from __future__ import annotations
from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type: TextType = text_type
        self.url: str | None = url
        pass

    def __eq__(self, other: object):
        if type(other) is not type(self):
            return False
        for prop in ["text", "text_type", "url"]:
            if self[prop] != other[prop]:
                return False
        return True

    def __getitem__(self, prop: str):
        if prop == "text":
            return self.text
        if prop == "text_type":
            return self.text_type
        if prop == "url":
            return self.url

    def __repr__(self) -> str:
        TEXT = self.text
        TEXT_TYPE = self.text_type.value
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"
