import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = TextNode("This is a text node", TextType.BOLD)
        self.node2 = TextNode("This is a text node", TextType.BOLD)
        self.node3 = TextNode("no", TextType.BOLD, None)
        self.node4 = TextNode("yes", TextType.LINK, "https://www.google.com")
        self.node5 = TextNode("yes", TextType.LINK, "https://www.google.com")
        self.node6 = TextNode("no", TextType.BOLD)
        return super().setUp()

    def test_id(self):
        self.assertEqual(self.node1, self.node1)

    def test_eq(self):
        self.assertEqual(self.node1, self.node2)

    def test_link_eq(self):
        self.assertEqual(self.node4, self.node5)

    def test_not_eq(self):
        self.assertNotEqual(self.node1, self.node4)

    def test_not_equal_None_url(self):
        self.assertNotEqual(self.node3, self.node4)

    def test_eq_None_url(self):
        self.assertEqual(self.node3, self.node6)


if __name__ == "__main__":
    unittest.main()
