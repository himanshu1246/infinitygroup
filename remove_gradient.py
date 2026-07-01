import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the exact gradient line I added
content = content.replace('<div class="absolute inset-0 z-20 bg-gradient-to-t from-surface-ivory/60 to-transparent md:hidden pointer-events-none"></div>', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Gradient removed.')
