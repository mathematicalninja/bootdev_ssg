### HTML NOT text
import unittest

from htmlnode import HTMLNode, HTMLType


class TestTextNode(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = HTMLNode(tag="a", value="a thing")
        self.node2 = HTMLNode()
        self.node3 = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.node4 = HTMLNode(children=[self.node1, self.node2, self.node3])
        return super().setUp()

    def test_print(self):
        print("node1: ")
        print(self.node1)
        print("node2: ")
        print(self.node2)
        print("node3: ")
        print(self.node3)
        print("node3: ")
        print(self.node4)


if __name__ == "__main__":
    unittest.main()
