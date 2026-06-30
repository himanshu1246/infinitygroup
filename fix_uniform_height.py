import re

filepath = r"d:\infinity website\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the mobile img tags to force a uniform height and object-cover, ensuring all slides match the tall Infinity Ikon look.
content = content.replace('class="w-full h-auto block"', 'class="w-full h-[60vh] object-cover object-center block"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Uniform image height applied.")
