import os
import glob
import re

def fix_project_heroes():
    for filepath in glob.glob(r'd:\infinity website\projects\*.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # We need to find the hero section.
        # It usually starts with: <section class="relative w-full h-auto flex items-center justify-center overflow-hidden bg-charcoal-black" data-aos="fade-up">
        # And ends with: </section>
        
        # Let's find the first <section> tag after <main>
        main_match = re.search(r'<main[^>]*>', content)
        if not main_match:
            continue
            
        start_idx = content.find('<section', main_match.end())
        end_idx = content.find('</section>', start_idx) + len('</section>')
        
        hero_html = content[start_idx:end_idx]
        
        # Extract the image URL
        img_match = re.search(r'<img src="([^"]+)"', hero_html)
        if not img_match:
            print(f"No image found in {filepath} hero")
            continue
        img_url = img_match.group(1)
        
        # Extract the badge (e.g. 🟡 ONGOING)
        # It's usually inside <div class="absolute top-28 right-margin-mobile ...">
        badge_html = ""
        badge_match = re.search(r'<div class="absolute top-28[^>]*>(.*?)</div>\s*</div>', hero_html, re.DOTALL)
        if badge_match:
            badge_html = badge_match.group(1).strip()
            # Wrap it in a nicer container that will sit on top of the image
            badge_html = f'''
            <div class="absolute top-6 right-6 z-20">
                {badge_html}
            </div>'''
            
        # Extract the text block
        # It's usually inside <div class="relative z-10 text-center ...">
        text_match = re.search(r'<div class="relative z-10 text-center[^>]*>(.*?)</div>\s*</section>', hero_html, re.DOTALL)
        if not text_match:
            print(f"No text block found in {filepath} hero")
            continue
        text_html = text_match.group(1).strip()
        
        # Rebuild the hero section
        # We will make it a flex column. Image on top, text below.
        # To make it "nice", we'll give the text area a very dark gradient or elegant padding.
        
        new_hero = f'''<section class="w-full flex flex-col bg-charcoal-black" data-aos="fade-up">
            <div class="relative w-full">
                <img src="{img_url}" class="w-full h-auto block" alt="Project Hero" />
                {badge_html}
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-transparent to-transparent opacity-80"></div>
            </div>
            
            <div class="w-full px-margin-mobile md:px-margin-desktop py-12 md:py-20 text-center max-w-container-max mx-auto relative z-10">
                {text_html}
            </div>
        </section>'''
        
        # Replace it in the content
        new_content = content[:start_idx] + new_hero + content[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Refactored hero in {os.path.basename(filepath)}")

fix_project_heroes()
