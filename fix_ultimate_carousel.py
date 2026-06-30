import re

filepath = r"d:\infinity website\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the section to use CSS Grid for stacking without absolute positioning collapse
content = content.replace('<section class="relative h-[80svh] md:h-screen flex items-center justify-center overflow-hidden bg-charcoal-black" data-aos="fade-up">', 
                          '<section class="grid grid-cols-1 grid-rows-1 relative w-full overflow-hidden bg-charcoal-black md:h-screen" data-aos="fade-up">')

# Also remove the hero-carousel div if it interferes, or just make it grid too.
# The original has: <div id="hero-carousel" class="absolute inset-0 w-full h-full">
# We must change it to grid-area or just remove it. Let's change it to block or grid.
content = content.replace('<div id="hero-carousel" class="absolute inset-0 w-full h-full">',
                          '<div id="hero-carousel" class="col-start-1 row-start-1 grid grid-cols-1 grid-rows-1 w-full h-full">')

# 2. Refactor the slides
def refactor_slide(match):
    image_url = match.group(1)
    title = match.group(2)
    desc = match.group(3)
    link = match.group(4)
    
    new_slide = f'''        <div class="carousel-slide col-start-1 row-start-1 w-full h-full transition-opacity duration-1000 z-10">
            <div class="flex flex-col md:block w-full h-full">
                <!-- Mobile Native Image (No Cropping) -->
                <div class="w-full relative md:hidden">
                    <img src="{image_url}" class="w-full h-auto block" alt="{title}" />
                    <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-transparent to-transparent"></div>
                </div>
                
                <!-- Desktop Background Overlay -->
                <div class="hidden md:block absolute inset-0 w-full h-full bg-cover bg-center opacity-70" style="background-image: url('{image_url}')"></div>
                <div class="hidden md:block absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/50 to-transparent"></div>
                
                <!-- Text Content -->
                <div class="w-full flex flex-col justify-center bg-charcoal-black py-8 px-6 md:bg-transparent md:absolute md:inset-0 z-10 text-center">
                    <div class="max-w-container-max mx-auto md:mt-20">
                        <span class="inline-block px-4 py-1 mb-4 md:mb-6 border border-primary-fixed/50 text-primary-fixed font-label-caps text-label-caps tracking-widest uppercase rounded-full backdrop-blur-sm">Featured Project</span>
                        <h1 class="font-display-lg text-display-lg text-on-primary mb-4 md:mb-6 max-w-4xl mx-auto leading-tight">{title}</h1>
                        <p class="font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-8 md:mb-10">{desc}</p>
                        <a href="{link}" class="inline-block btn-primary px-8 py-4 font-label-caps text-label-caps tracking-widest uppercase rounded">View Project</a>
                    </div>
                </div>
            </div>
        </div>'''
    return new_slide

# This regex matches the slide div and its inner content
# Because there are opacity classes that change via JS, we'll just match the whole div.
pattern = r'<div class="carousel-slide[^>]*>.*?url\(\'(.*?)\'\).*?<h1[^>]*>(.*?)<\/h1>\s*<p[^>]*>(.*?)<\/p>\s*<a href="(.*?)"[^>]*>.*?<\/a>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>'

content = re.sub(pattern, refactor_slide, content, flags=re.DOTALL)

# 3. Add opacity-100 to first slide, opacity-0 to others
content = content.replace('transition-opacity duration-1000 z-10', 'transition-opacity duration-1000 opacity-100 z-10', 1)
content = content.replace('transition-opacity duration-1000 z-10', 'transition-opacity duration-1000 opacity-0 pointer-events-none z-0')

# 4. Hide arrows on mobile
content = content.replace('class="absolute left-4 top-[30%] md:top-1/2', 'class="hidden md:block absolute left-4 top-1/2')
content = content.replace('class="absolute right-4 top-[30%] md:top-1/2', 'class="hidden md:block absolute right-4 top-1/2')

# 5. Position dots
content = content.replace('absolute bottom-10 left-1/2', 'absolute bottom-4 md:bottom-10 left-1/2')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ultimate carousel fix applied.")
