import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Slide 1
old_bg_1 = '<div class="hidden md:block absolute inset-0 bg-center bg-cover bg-no-repeat filter blur-3xl scale-110 opacity-40" style="background-image: url(\'/asset/infinity%20icon%20.png\');"></div>\n                '
content = content.replace(old_bg_1, '')
content = content.replace('class="relative z-10 w-full h-auto block md:h-[85vh] md:object-contain md:w-full drop-shadow-2xl" alt="Infinity Icon"', 'class="w-full h-[85vh] object-cover md:object-fill block w-full" alt="Infinity Icon"')
# Note: w-full h-auto on mobile might be fine, but if we want it to fit, let's keep it w-full h-[85vh] object-cover on mobile, or just w-full h-auto md:h-[85vh] md:object-fill md:w-full
content = content.replace('class="relative z-10 w-full h-auto block md:h-[85vh] md:object-contain md:w-full drop-shadow-2xl"', 'class="w-full h-[60vh] md:h-[85vh] object-fill block"')

# But wait, Slide 2 and 3 had slightly different original classes.
# Let's just use regex to remove the blur divs.
content = re.sub(r'<div class="hidden md:block absolute inset-0 bg-center bg-cover bg-no-repeat filter blur-3xl scale-110 opacity-40"[^>]*></div>\s*', '', content)

# And now replace all slide images with object-fill
# Find: <img src="/asset/..." class="relative z-10 w-full ... " alt="..." />
# Replace with: <img src="/asset/..." class="w-full h-[60vh] md:h-[85vh] object-fill block" alt="..." />

# Slide 1
content = re.sub(r'<img src="/asset/infinity%20icon%20.png" class="[^"]+" alt="Infinity Icon" />', r'<img src="/asset/infinity%20icon%20.png" class="w-full h-[60vh] md:h-[85vh] object-fill block" alt="Infinity Icon" />', content)

# Slide 2
content = re.sub(r'<img src="/asset/viviana.png" class="[^"]+" alt="Viviana" />', r'<img src="/asset/viviana.png" class="w-full h-[60vh] md:h-[85vh] object-fill block" alt="Viviana" />', content)

# Slide 3
content = re.sub(r'<img src="/asset/infinity%20icon.png" class="[^"]+" alt="Infinity Ikon" />', r'<img src="/asset/infinity%20icon.png" class="w-full h-[60vh] md:h-[85vh] object-fill block" alt="Infinity Ikon" />', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Changed to object-fill.")
