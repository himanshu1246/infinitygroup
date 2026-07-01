import os
import glob
import re

def fix_heights():
    for f in glob.glob(r'd:\infinity website\projects\*.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # We want to remove any h-[80vh], h-[60vh], md:h-auto, etc. 
        # and ensure the hero section is just h-auto so it fits the img exactly.
        # It's usually: class="relative h-[80vh] md:h-auto flex items-center justify-center overflow-hidden bg-charcoal-black"
        content = content.replace('h-[80vh] md:h-auto', 'w-full h-auto')
        content = content.replace('h-[60vh]', 'h-auto')
        content = content.replace('h-[100svh]', 'h-auto')
        content = content.replace('md:h-[100svh]', 'h-auto')
        content = content.replace('min-h-screen', 'h-auto')
        content = content.replace('h-screen', 'h-auto')
        
        # Also need to make sure the img is NOT absolute inset-0 anymore, but a regular block in flow!
        # Because we replaced the double-div with:
        # <img src="..." class="w-full h-auto block transform transition-transform duration-700 group-hover:scale-105" alt="Project Image" />
        # But wait! In the project page, there was an overlay:
        # <div class="absolute inset-0 bg-charcoal-black/30"></div>
        # And the text was absolute overlay!
        # If the text is absolute overlay, the img MUST dictate the height of the section.
        # Yes, since img is "w-full h-auto block" and is inside the section, the section will wrap its height perfectly.
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed {f}")

fix_heights()
