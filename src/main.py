from textnode import *

def main():
    text_node = TextNode("This is some anchor text","link","https://www.boot.dev")
    final = text_node.__repr__()
    print(final)



if __name__ == "__main__":
    main()