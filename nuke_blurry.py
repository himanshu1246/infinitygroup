import os
import re
import glob

def fix_all_blurry_images(base_dir):
    html_files = glob.glob(os.path.join(base_dir, '**/*.html'), recursive=True)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # 1. Replace the blurry background pattern with an img tag
        pattern = re.compile(
            r'<div class="absolute inset-0 w-full h-full bg-cover bg-center blur-3xl opacity-80 scale-125" style="background-image: url\(\'(.*?)\'\)"></div>\s*'
            r'<div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat\s*" style="background-image: url\(\'(.*?)\'\)"></div>',
            re.IGNORECASE | re.DOTALL
        )
        
        def replace_img(match):
            url = match.group(1)
            # Just use an img tag that takes natural height
            # and add the group-hover:scale-105 class so animations still work!
            return f'<img src="{url}" class="w-full h-auto block transform transition-transform duration-700 group-hover:scale-105" alt="Project Image" />'
            
        content = pattern.sub(replace_img, content)
        
        # 2. Remove fixed heights from containers to prevent solid black gaps
        
        # Remove h-[600px] from the Bento grid cards
        content = content.replace('h-[600px]', 'h-auto')
        
        # Remove h-64 from the projects.html grid cards
        content = content.replace(
            '<div class="h-64 bg-charcoal-black relative overflow-hidden">',
            '<div class="relative w-full h-auto overflow-hidden bg-charcoal-black">'
        )
        
        # Remove min-h-[400px] from about sections
        content = content.replace(
            'min-h-[400px]', ''
        )
        content = content.replace(
            '<div class="relative h-64 md:h-full  rounded-xl overflow-hidden shadow-2xl">',
            '<div class="relative w-full h-auto rounded-xl overflow-hidden shadow-2xl">'
        )
        # Handle cases where h-64 or min-h-[400px] were removed but spaces left
        content = re.sub(r'class="relative h-64 md:h-full\s+rounded-xl', 'class="relative w-full h-auto rounded-xl', content)
        
        # If the old double-div wrapper had group-hover:scale-105, it might still be there on the parent div.
        # But we added it to the img tag itself, so it's fine.
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {filepath}")

fix_all_blurry_images(r'd:\infinity website')
