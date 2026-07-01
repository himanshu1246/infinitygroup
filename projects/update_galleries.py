import os
import re
import urllib.parse

projects = {
    'infinity-icon-nerul.html': 'infinity ikon gallery',
    'infinity-icon-panvel.html': 'infinity icon gallery',
    'infinity-township-rasayani.html': 'infinity heights gallery'
}

base_dir = r'd:\infinity website\projects'

count = 0
for html_file, gallery_dir in projects.items():
    html_path = os.path.join(base_dir, html_file)
    gallery_path = os.path.join(base_dir, gallery_dir)
    
    if not os.path.exists(gallery_path):
        print(f"Directory {gallery_path} not found.")
        continue
        
    images = []
    for f in os.listdir(gallery_path):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
            images.append(f)
            
    images.sort()
    
    if not images:
        print(f"No images found in {gallery_path}")
        continue
        
    html_grid = '<div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6">\n'
    for img in images:
        img_url = f"/projects/{urllib.parse.quote(gallery_dir)}/{urllib.parse.quote(img)}"
        html_grid += f'                    <div class="h-64 border border-primary-container overflow-hidden group"><img src="{img_url}" alt="Project Gallery Image" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>\n'
    html_grid += '                </div>'
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the gallery block
    pattern = re.compile(r'<div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6">[\s\S]*?</div>(\s*</div>\s*</section>)')
    
    def repl(match):
        return html_grid + match.group(1)
        
    new_content = pattern.sub(repl, content, count=1)
    
    if new_content != content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {html_file}")
    else:
        print(f"No match found in {html_file}")

print(f"Total files updated: {count}")
