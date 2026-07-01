with open('main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix link color in modal
content = content.replace('class="text-primary-fixed hover:underline">Terms & Conditions',
                          'class="text-charcoal-black underline font-bold hover:text-primary-container">Terms & Conditions')
content = content.replace('class="text-primary-fixed hover:underline">Privacy Policy',
                          'class="text-charcoal-black underline font-bold hover:text-primary-container">Privacy Policy')

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)
