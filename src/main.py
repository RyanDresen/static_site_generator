from textnode import *

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK.value,"https://www.boot.dev")
    final = text_node.__repr__()
    print(final)


if __name__ == "__main__":
    main()