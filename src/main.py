from textnode import TextNode, TextType


def main():
    tn = TextNode("This is some anchor text", TextType("link"), "https://www.boot.dev")

    print(tn)

    pass


if __name__ == "__main__":
    main()
