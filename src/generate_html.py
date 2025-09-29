import os
from block_markdown import markdown_to_blocks, markdown_to_htmlnode


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        line = block.strip()
        if line.startswith("# "):
            level = 0
            for char in line:
                if char == "#":
                    level += 1
                else:
                    break
            if level == 1:
                return line[1:].strip()
    raise Exception("no header")


def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}:")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        html_string = f.read()
    html_node = markdown_to_htmlnode(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    html_string = html_string.replace("{{ Title }}", title)  
    html_string = html_string.replace("{{ Content }}", html) 

    html_string = html_string.replace('href="/', f'href="{base_path}')
    html_string = html_string.replace('src="/', f'src="{base_path}')


    parent = os.path.dirname(dest_path)
    if parent:
        os.makedirs(parent, exist_ok=True) 
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_string)
    print(f"{dest_path} done.")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    full_source_path = os.path.join(dir_path_content)
    full_template_path = os.path.join(template_path)
    full_dest_path = os.path.join(dest_dir_path)
    print(f"Entering directory: {full_source_path}:") # Good for debugging!

    contents = os.listdir(full_source_path)
    for item in contents:
        full_path_to_item = os.path.join(full_source_path, item)
        full_path_to_item_dest = os.path.join(full_dest_path, item)

        if os.path.isfile(full_path_to_item) and full_path_to_item.endswith(".md"):
            full_path_to_item_dest = full_path_to_item_dest[:-2] + "html"
            generate_page(full_path_to_item, full_template_path, full_path_to_item_dest, base_path)
        elif os.path.isdir(full_path_to_item):
            os.mkdir(full_path_to_item_dest)
            generate_pages_recursive(full_path_to_item, template_path, full_path_to_item_dest, base_path)
    print(f"{full_source_path} done")
