import os
import re
import urllib.parse

# Path to the README.md file
markdown_file = 'README.md'

# Directory containing images
image_dir = 'img'

# Regex pattern to find broken image links
pattern = re.compile(r'!\[.*?\]\((.*?)\)')

def update_image_links(markdown_file, image_dir):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all broken image links
    broken_links = pattern.findall(content)

    # Iterate over broken links and update them with ordered image filenames
    for index, link in enumerate(broken_links):
        # Generate the new image filename based on the index
        if index == 0:
            image_filename = 'Untitled.png'
        else:
            image_filename = f'Untitled {index}.png'
        
        # URL encode the image filename
        encoded_image_filename = urllib.parse.quote(image_filename)
        
        # New image path
        new_image_path = os.path.join(image_dir, encoded_image_filename)
        
        # Ensure the path uses forward slashes
        new_image_path = new_image_path.replace('\\', '/')
        
        # Replace old link with new path
        content = content.replace(link, new_image_path, 1)

    # Write the updated content back to the file
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(content)

# Run the function
update_image_links(markdown_file, image_dir)
