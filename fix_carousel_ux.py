import re

filepath = r"d:\infinity website\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the section height to be taller on mobile for the split layout
content = content.replace('<section class="relative h-[60vh] md:h-screen flex items-center justify-center overflow-hidden bg-charcoal-black" data-aos="fade-up">', 
                          '<section class="relative h-[90svh] md:h-screen flex items-center justify-center overflow-hidden bg-charcoal-black" data-aos="fade-up">')

# 2. Refactor the slides
def refactor_slide(match):
    image_url = match.group(1)
    title = match.group(2)
    desc = match.group(3)
    link = match.group(4)
    
    new_slide = f'''            <div class="flex flex-col md:block w-full h-full">
                <!-- Mobile Split / Desktop Background -->
                <div class="relative w-full h-[50%] md:h-full md:absolute md:inset-0">
                    <div class="w-full h-full bg-cover bg-center opacity-100 md:opacity-70" style="background-image: url('{image_url}')"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-charcoal-black to-transparent md:via-charcoal-black/50"></div>
                </div>
                <!-- Mobile Text Area / Desktop Overlay -->
                <div class="relative w-full h-[50%] flex items-center justify-center bg-charcoal-black md:bg-transparent md:absolute md:inset-0 z-10">
                    <div class="text-center px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto md:mt-20">
                        <span class="inline-block px-4 py-1 mb-4 md:mb-6 border border-primary-fixed/50 text-primary-fixed font-label-caps text-label-caps tracking-widest uppercase rounded-full backdrop-blur-sm">Featured Project</span>
                        <h1 class="font-display-lg text-display-lg text-on-primary mb-4 md:mb-6 max-w-4xl mx-auto leading-tight" data-aos="zoom-out-down">{title}</h1>
                        <p class="font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-8 md:mb-10">{desc}</p>
                        <a href="{link}" class="inline-block btn-primary px-8 py-4 font-label-caps text-label-caps tracking-widest uppercase rounded">View Project</a>
                    </div>
                </div>
            </div>'''
    return new_slide

# This regex matches the inner content of a carousel-slide
pattern = r'<div class="bg-\[length:100%_auto\].*?url\(\'(.*?)\'\).*?<h1.*?>(.*?)<\/h1>\s*<p.*?>(.*?)<\/p>\s*<a href="(.*?)".*?<\/a>\s*<\/div>\s*<\/div>'

content = re.sub(pattern, refactor_slide, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI/UX layout fixed for mobile carousel.")
