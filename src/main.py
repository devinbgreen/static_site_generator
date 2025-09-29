from copy_static import stage_static
from generate_html import generate_pages_recursive
import sys


def main():
    print(sys.argv)
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    stage_static("static", "docs")
    #Generate a page from content/index.md using template.html and write it to public/index.html
    generate_pages_recursive("content", "template.html", "docs", base_path)


main()
