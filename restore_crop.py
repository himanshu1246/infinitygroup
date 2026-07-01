import os

def restore_desktop_crop():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to add the cropped classes back to the images in the carousel
    # Slide 1
    content = content.replace(
        '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block" alt="Infinity Icon" />',
        '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block md:w-full md:h-[85vh] md:object-cover" alt="Infinity Icon" />'
    )
    
    # Slide 2
    content = content.replace(
        '<img src="/asset/viviana.png" class="w-full h-full object-cover block" alt="Viviana" />',
        '<img src="/asset/viviana.png" class="w-full h-full object-cover block md:w-full md:h-[85vh] md:object-cover" alt="Viviana" />'
    )
    
    # Slide 3
    content = content.replace(
        '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block" alt="Infinity Ikon" />',
        '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block md:w-full md:h-[85vh] md:object-cover" alt="Infinity Ikon" />'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Restored the cropped desktop layout.")

restore_desktop_crop()
