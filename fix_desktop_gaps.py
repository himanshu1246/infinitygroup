import os

def fix_desktop_carousel_gaps():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The old desktop classes that caused left/right gaps because of w-auto
    old_classes = "md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto"
    
    # The new desktop classes that force full width and fixed height, using object-cover to prevent distortion
    new_classes = "md:w-full md:h-[85vh] md:object-cover"
    
    content = content.replace(old_classes, new_classes)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed desktop carousel gaps.")

fix_desktop_carousel_gaps()
