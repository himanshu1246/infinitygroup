import os
import re

def fix_opacities(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix the foreground image (bg-contain). Remove opacity-60, opacity-70, opacity-80, etc.
    # We will look for bg-contain and remove opacity-\d+ from that specific div tag.
    def remove_opacity(match):
        tag = match.group(0)
        tag = re.sub(r'\bopacity-\d+\b', '', tag)
        return tag

    content = re.sub(r'<div[^>]*bg-contain[^>]*>', remove_opacity, content)

    # 2. Enhance the background blur to fill gaps beautifully.
    # Change blur-xl to blur-3xl, opacity-40 to opacity-80, scale-110 to scale-125
    def enhance_blur(match):
        tag = match.group(0)
        tag = tag.replace('blur-xl', 'blur-3xl')
        tag = tag.replace('blur-2xl', 'blur-3xl')
        tag = re.sub(r'\bopacity-\d+\b', 'opacity-80', tag)
        tag = tag.replace('scale-110', 'scale-125')
        return tag

    content = re.sub(r'<div[^>]*bg-cover[^>]*blur-[^>]*>', enhance_blur, content)

    # 3. For native img tags (mobile hero), do the same logic if they exist.
    # Foreground object-contain:
    content = re.sub(r'<img[^>]*object-contain[^>]*>', remove_opacity, content)
    # Background object-cover with blur:
    content = re.sub(r'<img[^>]*object-cover[^>]*blur-[^>]*>', enhance_blur, content)

    # Note: I should make sure I don't remove opacity from buttons or UI elements, 
    # but the regex specifically targets tags containing bg-contain, bg-cover+blur, object-contain, object-cover+blur.
    # This is highly safe.

    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed opacities in: {filepath}")

if __name__ == "__main__":
    for root, dirs, files in os.walk(r'd:\infinity website'):
        for file in files:
            if file.endswith('.html'):
                fix_opacities(os.path.join(root, file))
