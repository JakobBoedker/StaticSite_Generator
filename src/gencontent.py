import os
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path):
            # If this is a markdown file
            if entry_path.endswith(".md"):
                # Figure out the destination path
                # Replace .md with .html in the filename
                output_filename = entry.replace(".md", ".html")
                output_path = os.path.join(dest_dir_path, output_filename)

                # Make sure the destination directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Use your existing generate_page function
                generate_page(entry_path, template_path, output_path, basepath)
        else:
            # This is a directory, so process it recursively
            # Create the corresponding destination directory
            new_dest_dir = os.path.join(dest_dir_path, entry)

            # Make sure it exists
            os.makedirs(new_dest_dir, exist_ok=True)

            # Recursively process this directory
            generate_pages_recursive(entry_path, template_path, new_dest_dir, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
