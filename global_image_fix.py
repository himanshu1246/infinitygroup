import os
import re

base_dir = r"d:\infinity website"

# Regex Patterns and Replacements

# Pattern 1: Hero Banners
pattern_hero = r'<div class="bg-cover bg-center w-full h-full opacity-60" style="background-image: url\(\'(.*?)\'\)"><\/div>'
replacement_hero = r'''<div class="absolute inset-0 w-full h-full overflow-hidden bg-charcoal-black">
    <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-xl opacity-40 scale-110" style="background-image: url('\1')"></div>
    <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat opacity-60" style="background-image: url('\1')"></div>
</div>'''

# Pattern 2: Desktop Carousel
pattern_carousel = r'<div class="hidden md:block absolute inset-0 w-full h-full bg-cover bg-center opacity-70" style="background-image: url\(\'(.*?)\'\)"><\/div>'
replacement_carousel = r'''<div class="hidden md:block absolute inset-0 w-full h-full overflow-hidden bg-charcoal-black">
    <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-xl opacity-40 scale-110" style="background-image: url('\1')"></div>
    <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat opacity-70" style="background-image: url('\1')"></div>
</div>'''

# Pattern 3: Gallery Cards (With Hover)
pattern_gallery = r'<div class="bg-cover bg-center w-full h-full transform group-hover:scale-105 transition-transform duration-700"(.*?)style="background-image: url\(\'(.*?)\'\)"><\/div>'
replacement_gallery = r'''<div class="relative w-full h-full overflow-hidden bg-charcoal-black group-hover:scale-105 transform transition-transform duration-700"\1>
    <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-xl opacity-40 scale-110" style="background-image: url('\2')"></div>
    <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat" style="background-image: url('\2')"></div>
</div>'''

# Pattern 4: Gallery Cards (Without Hover)
pattern_gallery2 = r'<div class="bg-cover bg-center w-full h-full"(.*?)style="background-image: url\(\'(.*?)\'\)"><\/div>'
replacement_gallery2 = r'''<div class="relative w-full h-full overflow-hidden bg-charcoal-black"\1>
    <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-xl opacity-40 scale-110" style="background-image: url('\2')"></div>
    <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat" style="background-image: url('\2')"></div>
</div>'''

# Pattern 5: Projects Grid Cards
pattern_projects = r'<div class="h-64 bg-charcoal-black relative bg-cover bg-center" style="background-image: url\(\'(.*?)\'\)">'
replacement_projects = r'''<div class="h-64 bg-charcoal-black relative overflow-hidden">
    <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-xl opacity-40 scale-110" style="background-image: url('\1')"></div>
    <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat" style="background-image: url('\1')"></div>'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = re.sub(pattern_hero, replacement_hero, content)
    content = re.sub(pattern_carousel, replacement_carousel, content)
    content = re.sub(pattern_gallery, replacement_gallery, content)
    content = re.sub(pattern_gallery2, replacement_gallery2, content)
    content = re.sub(pattern_projects, replacement_projects, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

# Iterate through all HTML files
for root, _, files in os.walk(base_dir):
    if "stitch_infinity_developers_digital_hub" in root: # Skip backup folder
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("Global replacement complete.")
