import os

def add_desktop_ambient_backgrounds():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the current img tags with the ambient background div + the img tag (with relative z-10 added).

    # Slide 1
    slide1_img_old = '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto" alt="Infinity Icon" />'
    slide1_new = '''<!-- Desktop Ambient Background -->
                <div class="hidden md:block absolute inset-0 w-full h-full bg-cover bg-center bg-no-repeat blur-2xl opacity-40 scale-110" style="background-image: url('/asset/infinity%20icon%20.png');"></div>
                <img src="/asset/infinity%20icon%20.png" class="relative z-10 w-full h-auto block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto drop-shadow-2xl" alt="Infinity Icon" />'''
    content = content.replace(slide1_img_old, slide1_new)

    # Slide 2
    slide2_img_old = '<img src="/asset/viviana.png" class="w-full h-full object-cover block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto" alt="Viviana" />'
    slide2_new = '''<!-- Desktop Ambient Background -->
                <div class="hidden md:block absolute inset-0 w-full h-full bg-cover bg-center bg-no-repeat blur-2xl opacity-40 scale-110" style="background-image: url('/asset/viviana.png');"></div>
                <img src="/asset/viviana.png" class="relative z-10 w-full h-full object-cover block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto drop-shadow-2xl" alt="Viviana" />'''
    content = content.replace(slide2_img_old, slide2_new)

    # Slide 3
    slide3_img_old = '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto" alt="Infinity Ikon" />'
    slide3_new = '''<!-- Desktop Ambient Background -->
                <div class="hidden md:block absolute inset-0 w-full h-full bg-cover bg-center bg-no-repeat blur-2xl opacity-40 scale-110" style="background-image: url('/asset/infinity%20icon.png');"></div>
                <img src="/asset/infinity%20icon.png" class="relative z-10 w-full h-full object-cover block md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto drop-shadow-2xl" alt="Infinity Ikon" />'''
    content = content.replace(slide3_img_old, slide3_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Added ambient background to all carousel slides.")

add_desktop_ambient_backgrounds()
