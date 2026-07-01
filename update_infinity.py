import re

with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Isolate the Infinity card and make changes inside it
def replace_in_infinity_card(match):
    card = match.group(0)
    card = card.replace('> Kharghar</div>', '> Upper Kharghar</div>')
    card = card.replace('> 50+ Units</div>', '> 1000+ Units</div>')
    return card

content = re.sub(r'(<h3 class="font-headline-lg text-headline-lg text-primary-container mb-1">Infinity</h3>[\s\S]*?</div>\s*</div>)', replace_in_infinity_card, content)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('projects/infinity-vandhan-heights-kharghar.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('at Kharghar, Navi Mumbai', 'at Upper Kharghar, Navi Mumbai')
content = content.replace('node of Kharghar, Navi Mumbai', 'node of Upper Kharghar, Navi Mumbai')
content = content.replace('Kharghar Railway Station', 'Upper Kharghar Railway Station')
content = content.replace('Central Park Kharghar', 'Central Park Upper Kharghar')
content = content.replace('Units: 50+', 'Units: 1000+')
content = content.replace('<div class="font-headline-md text-headline-md text-charcoal-black">50+</div>', '<div class="font-headline-md text-headline-md text-charcoal-black">1000+</div>')

# Remove the Project Gallery section
# The section starts with <section... and contains "Project Gallery" and ends with </section>
pattern = r'<section class="py-16 px-margin-mobile md:px-margin-desktop bg-surface-container-lowest"[^>]*>\s*<div[^>]*>\s*<h2[^>]*>Project Gallery</h2>[\s\S]*?</section>\s*'
content = re.sub(pattern, '', content)

with open('projects/infinity-vandhan-heights-kharghar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Infinity project updated.")
