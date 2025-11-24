import os
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(f" * generating html from: {dir_path_content} -> {dest_dir_path}")

    # Ensure destination dir exists
    os.makedirs(dest_dir_path, exist_ok=True)

    for item in os.listdir(dir_path_content):
        current_full_path = os.path.join(dir_path_content, item)

        # If it's a directory, recurse into it
        if os.path.isdir(current_full_path):
            new_dest_dir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(current_full_path, template_path, new_dest_dir, basepath)

        # If it's a markdown file, generate an HTML file
        elif os.path.isfile(current_full_path) and item.endswith(".md"):
            with open(current_full_path, "r", encoding="utf-8") as from_file:
                markdown_content = from_file.read()

            with open(template_path, "r", encoding="utf-8") as template_file:
                template = template_file.read()

            node = markdown_to_html_node(markdown_content)
            html = node.to_html()

            title = extract_title(markdown_content)
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)
            template = template.replace("href=/", "href={basepath}")
            template = template.replace("src=/", "src={basepath}")

            # e.g. "index.md" -> "index.html"
            base_name, _ = os.path.splitext(item)
            dest_file_path = os.path.join(dest_dir_path, base_name + ".html")

            with open(dest_file_path, "w", encoding="utf-8") as to_file:
                to_file.write(template)

            print(f"   - generated {dest_file_path}")
        else:
            # Non-markdown files in content/ are ignored
            pass
    

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
