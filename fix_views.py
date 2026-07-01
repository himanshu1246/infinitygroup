import re

def fix_sections():
    # 1. Fix about.html
    about_path = r'd:\infinity website\about.html'
    with open(about_path, 'r', encoding='utf-8') as f:
        about_content = f.read()
    
    # Change h-[80vh] md:h-auto to just h-[80vh] or md:h-[80vh]
    about_content = about_content.replace('h-[80vh] md:h-auto', 'h-[80vh]')
    
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(about_content)
        
    # 2. Fix index.html carousel
    index_path = r'd:\infinity website\index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    # Remove ambient backgrounds
    # <!-- Desktop Ambient Background -->
    # <div class="hidden md:block absolute inset-0 ..."></div>
    index_content = re.sub(r'<!-- Desktop Ambient Background -->\s*<div class="hidden md:block absolute inset-0[^>]*></div>\s*', '', index_content)
    
    # Remove desktop constraints from images
    # class="relative z-10 w-full h-auto block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto drop-shadow-2xl"
    # Or for inactive: class="relative z-10 w-full h-full object-cover block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto drop-shadow-2xl"
    
    # We just replace the desktop classes.
    index_content = index_content.replace('md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto drop-shadow-2xl', '')
    index_content = index_content.replace('md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto', '')
    
    # We might also have 'relative z-10' on the images. We can keep it or remove it, it shouldn't hurt.
    # But let's clean it up to be exactly like before.
    index_content = index_content.replace('class="relative z-10 w-full h-auto block "', 'class="w-full h-auto block"')
    index_content = index_content.replace('class="relative z-10 w-full h-full object-cover block "', 'class="w-full h-full object-cover block"')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
        
    print("Fixed about.html and index.html")

fix_sections()
