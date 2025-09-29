from textnode import TextNode, TextType
from copy_static import stage_static
from generate_html import generate_pages_recursive


def main():
    
    stage_static("static", "public")
    #Generate a page from content/index.md using template.html and write it to public/index.html
    generate_pages_recursive("content", "template.html", "public")


main()
