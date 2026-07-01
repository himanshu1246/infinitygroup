import os
import re

def rebuild_carousel(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will entirely replace the hero section
    
    # 1. Replace the section wrapper
    content = content.replace(
        '<section class="grid grid-cols-1 grid-rows-1 relative w-full overflow-hidden bg-charcoal-black h-[100svh]" data-aos="fade-up">',
        '<section class="relative w-full overflow-hidden bg-charcoal-black" data-aos="fade-up">'
    )
    
    # 2. Replace the carousel container
    content = content.replace(
        '<div id="hero-carousel" class="col-start-1 row-start-1 grid grid-cols-1 grid-rows-1 w-full h-full">',
        '<div id="hero-carousel" class="relative w-full h-auto">'
    )
    
    # 3. Slide 1 (Active)
    content = content.replace(
        '''        <!-- Slide 1: Infinity Icon -->
        <div class="carousel-slide col-start-1 row-start-1 w-full h-full transition-opacity duration-1000 opacity-100 z-10">
            <div class="relative w-full h-full overflow-hidden bg-charcoal-black">
                <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-3xl opacity-80 scale-125" style="background-image: url('/asset/infinity%20icon%20.png')"></div>
                <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat" style="background-image: url('/asset/infinity%20icon%20.png')"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>''',
        '''        <!-- Slide 1: Infinity Icon -->
        <div class="carousel-slide relative w-full h-auto transition-opacity duration-1000 opacity-100 z-10">
            <div class="relative w-full h-auto overflow-hidden bg-charcoal-black">
                <img src="/asset/infinity%20icon%20.png" class="w-full h-auto block" alt="Infinity Icon" />
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>'''
    )
    
    # 4. Slide 2 (Inactive)
    content = content.replace(
        '''        <!-- Slide 2: Viviana -->
        <div class="carousel-slide col-start-1 row-start-1 w-full h-full transition-opacity duration-1000 opacity-0 pointer-events-none z-0">
            <div class="relative w-full h-full overflow-hidden bg-charcoal-black">
                <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-3xl opacity-80 scale-125" style="background-image: url('/asset/viviana.png')"></div>
                <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat" style="background-image: url('/asset/viviana.png')"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>''',
        '''        <!-- Slide 2: Viviana -->
        <div class="carousel-slide absolute inset-0 w-full h-full transition-opacity duration-1000 opacity-0 pointer-events-none z-0">
            <div class="relative w-full h-full overflow-hidden bg-charcoal-black">
                <img src="/asset/viviana.png" class="w-full h-full object-cover block" alt="Viviana" />
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>'''
    )
    
    # 5. Slide 3 (Inactive)
    content = content.replace(
        '''        <!-- Slide 3: Infinity Ikon -->
        <div class="carousel-slide col-start-1 row-start-1 w-full h-full transition-opacity duration-1000 opacity-0 pointer-events-none z-0">
            <div class="relative w-full h-full overflow-hidden bg-charcoal-black">
                <div class="absolute inset-0 w-full h-full bg-cover bg-center blur-3xl opacity-80 scale-125" style="background-image: url('/asset/infinity%20icon.png')"></div>
                <div class="absolute inset-0 w-full h-full bg-contain bg-center bg-no-repeat" style="background-image: url('/asset/infinity%20icon.png')"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>''',
        '''        <!-- Slide 3: Infinity Ikon -->
        <div class="carousel-slide absolute inset-0 w-full h-full transition-opacity duration-1000 opacity-0 pointer-events-none z-0">
            <div class="relative w-full h-full overflow-hidden bg-charcoal-black">
                <img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block" alt="Infinity Ikon" />
                <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>'''
    )

    # 6. Update JS updateSlide()
    old_js = '''                    slide.classList.remove('opacity-0', 'pointer-events-none', 'z-0');
                    slide.classList.add('opacity-100', 'z-10');'''
    new_js = '''                    slide.classList.remove('opacity-0', 'pointer-events-none', 'z-0', 'absolute', 'inset-0', 'h-full');
                    slide.classList.add('opacity-100', 'z-10', 'relative', 'h-auto');
                    
                    // Update inner image class for active state
                    let img = slide.querySelector('img');
                    if(img) {
                        img.classList.remove('h-full', 'object-cover');
                        img.classList.add('h-auto');
                    }'''
    content = content.replace(old_js, new_js)

    old_js2 = '''                    slide.classList.remove('opacity-100', 'z-10');
                    slide.classList.add('opacity-0', 'pointer-events-none', 'z-0');'''
    new_js2 = '''                    slide.classList.remove('opacity-100', 'z-10', 'relative', 'h-auto');
                    slide.classList.add('opacity-0', 'pointer-events-none', 'z-0', 'absolute', 'inset-0', 'h-full');
                    
                    // Update inner image class for inactive state
                    let img = slide.querySelector('img');
                    if(img) {
                        img.classList.remove('h-auto');
                        img.classList.add('h-full', 'object-cover');
                    }'''
    content = content.replace(old_js2, new_js2)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

rebuild_carousel(r'd:\infinity website\index.html')
