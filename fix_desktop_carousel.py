import os

def fix_desktop_carousel_size():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to add the desktop responsive classes to the carousel images
    desktop_classes = "md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto"
    
    # 1. Slide 1 (active)
    content = content.replace(
        '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block" alt="Infinity Icon" />',
        f'<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block {desktop_classes}" alt="Infinity Icon" />'
    )
    
    # 2. Slide 2 (inactive)
    content = content.replace(
        '<img src="/asset/viviana.png" class="w-full h-full object-cover block" alt="Viviana" />',
        f'<img src="/asset/viviana.png" class="w-full h-full object-cover block {desktop_classes}" alt="Viviana" />'
    )
    
    # 3. Slide 3 (inactive)
    content = content.replace(
        '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block" alt="Infinity Ikon" />',
        f'<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block {desktop_classes}" alt="Infinity Ikon" />'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed desktop carousel image size.")

fix_desktop_carousel_size()
