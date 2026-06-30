import re

filepath = r"d:\infinity website\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce overall hero height on mobile to eliminate massive black space
content = content.replace('h-[90svh] md:h-screen', 'h-[80svh] md:h-screen')

# 2. Adjust the split layout: Make image take 60% and text 40% (removes text gaps)
# Find the image containers
content = content.replace('relative w-full h-[50%] md:h-full md:absolute md:inset-0', 
                          'relative w-full h-[55%] md:h-full md:absolute md:inset-0')

# Find the text containers
content = content.replace('relative w-full h-[50%] flex items-center justify-center bg-charcoal-black md:bg-transparent md:absolute md:inset-0 z-10', 
                          'relative w-full h-[45%] flex flex-col justify-start pt-6 md:pt-0 md:justify-center bg-charcoal-black md:bg-transparent md:absolute md:inset-0 z-10')

# 3. Ensure bg-cover is used but shifted slightly down so buildings aren't cut at the top, or use a better object-fit equivalent.
# The user wants NO cutting, but also NO black space. bg-cover with bg-center is the only way to fill the box.
# By making the box 55% of 80svh (44svh), it matches the building ratio much better.
content = content.replace('bg-contain md:bg-cover bg-center bg-no-repeat', 
                          'bg-cover bg-top md:bg-center bg-no-repeat')

# 4. Move arrows slightly up since the image takes 55%
content = content.replace('top-[25%] md:top-1/2', 'top-[30%] md:top-1/2')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed black space and optimized layout.")
