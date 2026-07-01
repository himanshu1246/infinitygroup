import os
import re

def fix_all_images():
    base_dir = r"d:\infinity website"
    
    html_files = [
        os.path.join(base_dir, "about.html"),
        os.path.join(base_dir, "projects.html"),
    ]
    projects_dir = os.path.join(base_dir, "projects")
    if os.path.exists(projects_dir):
        for f in os.listdir(projects_dir):
            if f.endswith(".html"):
                html_files.append(os.path.join(projects_dir, f))
                
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Pattern to match the blurry background + contain background divs
        # We need to capture the image URL.
        pattern = re.compile(
            r'<div class="absolute inset-0 w-full h-full bg-cover bg-center blur-3xl opacity-80 scale-125" style="background-image: url\(\'(.*?)\'\)"></div>\s*'
            r'<div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat\s*" style="background-image: url\(\'(.*?)\'\)"></div>',
            re.IGNORECASE | re.DOTALL
        )
        
        # Replace the pattern with a simple img tag that perfectly fits its container
        def replace_img(match):
            url = match.group(1)
            # Just use an img tag that takes natural height
            return f'<img src="{url}" class="w-full h-auto block" alt="Project Image" />'
            
        new_content = pattern.sub(replace_img, content)
        
        # Now we need to remove the fixed heights from the parent containers so they wrap perfectly!
        # 1. Project cards in projects.html: <div class="h-64 bg-charcoal-black relative overflow-hidden">
        new_content = new_content.replace(
            '<div class="h-64 bg-charcoal-black relative overflow-hidden">',
            '<div class="relative w-full h-auto overflow-hidden bg-charcoal-black">'
        )
        
        # 2. Hero sections in project pages: <div class="relative w-full overflow-hidden bg-charcoal-black h-[60vh] md:h-[100svh]"> or similar
        # Let's just use regex to remove any fixed height classes from sections/divs that wrap these images.
        # Actually, let's target the known ones.
        new_content = re.sub(
            r'class="grid grid-cols-1 grid-rows-1 relative w-full overflow-hidden bg-charcoal-black h-\[100svh\]"',
            r'class="relative w-full overflow-hidden bg-charcoal-black"',
            new_content
        )
        
        new_content = new_content.replace(
            '<div id="hero-carousel" class="col-start-1 row-start-1 grid grid-cols-1 grid-rows-1 w-full h-full">',
            '<div id="hero-carousel" class="relative w-full h-auto">'
        )
        
        new_content = new_content.replace(
            '<div class="carousel-slide col-start-1 row-start-1 w-full h-full',
            '<div class="carousel-slide relative w-full h-auto'
        )

        # For inactive slides, we might need absolute w-full h-full
        # But wait, if they are project pages, they usually only have 1 image!
        # If it has only 1 image, it won't have inactive slides.

        # What if it's the about page?
        new_content = new_content.replace(
            '<div class="relative h-64 md:h-full min-h-[400px] rounded-xl overflow-hidden shadow-2xl">',
            '<div class="relative w-full h-auto rounded-xl overflow-hidden shadow-2xl">'
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("Fixed all images across the site!")

fix_all_images()
