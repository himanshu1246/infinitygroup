with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# In projects.html, replace the RERA line for Infinity Heights
# Find the Infinity Heights section
content = re.sub(r'(<h3 class="font-headline-lg text-headline-lg text-primary-container mb-1">Infinity Heights</h3>[\s\S]*?)RERA: \[Pending\]', r'\1Status: CC Received', content)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('projects/infinity-township-rasayani.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace RERA line
content = content.replace('RERA Registration: [TO BE FILLED — add RERA number here]', 'Status: CC Received')

# Maybe also add CC Received as a tag
tag_to_add = '<div class="px-6 py-2 border border-border-muted bg-surface text-charcoal-black font-label-caps text-label-caps rounded uppercase font-bold text-green-700 border-green-700 bg-green-50">CC Received</div>'
content = content.replace('<div class="flex flex-wrap justify-center gap-4 mb-8">', '<div class="flex flex-wrap justify-center gap-4 mb-8">\n                    ' + tag_to_add)

with open('projects/infinity-township-rasayani.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("CC updated.")
