import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace section background
content = content.replace('<section class="relative w-full overflow-hidden bg-charcoal-black" data-aos="fade-up">',
                          '<section class="relative w-full overflow-hidden bg-surface-ivory" data-aos="fade-up">')

# Replace slide backgrounds
content = content.replace('overflow-hidden bg-charcoal-black">',
                          'overflow-hidden bg-surface-ivory">')

# Replace gradients
content = content.replace('bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent',
                          'bg-gradient-to-t from-surface-ivory via-surface-ivory/80 to-transparent')

# Replace pill text
content = content.replace('border border-primary-fixed/50 text-primary-fixed',
                          'border border-primary-container text-primary-container')

# Replace h1 text color
content = content.replace('text-on-primary mb-2 md:mb-6 max-w-4xl',
                          'text-charcoal-black mb-2 md:mb-6 max-w-4xl')

# Replace paragraph text color
content = content.replace('text-secondary-fixed/90 max-w-2xl',
                          'text-on-surface-variant max-w-2xl')

# Replace control arrows color
content = content.replace('z-20 text-white hover:text-primary-container',
                          'z-20 text-charcoal-black hover:text-primary-container')

# Replace indicators color
content = content.replace('rounded-full bg-white opacity-100',
                          'rounded-full bg-charcoal-black opacity-100')
content = content.replace('rounded-full bg-white opacity-50 hover:opacity-100',
                          'rounded-full bg-charcoal-black opacity-50 hover:opacity-100')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html carousel styles')
