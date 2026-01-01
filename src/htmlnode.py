from __future__ import annotations
from typing import Literal, Tuple
from enum import Enum

from src.tagTypes import HTML_TAG


class HTMLType(Enum):
    pass


class HTMLNode:
    def __init__(
        self,  #
        tag: HTML_TAG | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag: HTML_TAG | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self, props: dict[str, str]) -> str:
        ks = props.keys()
        if len(ks) == 0:
            return ""
        r_list: list[str] = []
        for k in sorted(ks):
            # BUG: possible string quote mark errors.
            r_list.append(f'{k}="{props[k]}"')
            pass
        pass
        return " ".join(r_list)

    def get_tags(
        self,
    ) -> Tuple[
        str,
        Literal["special", "singular", "xml", "raw"],
    ]:
        match self.tag:
            case _:
                # defaults to raw text, if tag == None
                return "raw text", "raw"

    def __repr__(self) -> str:
        r: list[str] = [
            "self.tag: " + self.tag.__repr__(),
            "self.value: " + self.value.__repr__(),
            "self.children: " + self.children.__repr__(),
            "self.props: " + self.props.__repr__(),
        ]

        return "\n".join(r)
