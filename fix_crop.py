import os

def fix_desktop_crop():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the carousel images and append the md: classes
    # We will just replace the exact img tags for the three slides.
    
    # Slide 1
    content = content.replace(
        '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block" alt="Infinity Icon" />',
        '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block md:h-[85vh] md:object-cover md:w-full" alt="Infinity Icon" />'
    )
    
    # Slide 2
    content = content.replace(
        '<img src="/asset/viviana.png" class="w-full h-full object-cover block" alt="Viviana" />',
        '<img src="/asset/viviana.png" class="w-full h-full object-cover block md:h-[85vh] md:object-cover md:w-full" alt="Viviana" />'
    )
    
    # Slide 3
    content = content.replace(
        '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block" alt="Infinity Ikon" />',
        '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block md:h-[85vh] md:object-cover md:w-full" alt="Infinity Ikon" />'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Added desktop crop classes to carousel images.")

fix_desktop_crop()
