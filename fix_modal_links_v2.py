with open('main.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="text-primary-fixed hover:underline">Terms & Conditions',
                          'class="text-primary-container font-semibold hover:underline hover:text-charcoal-black">Terms & Conditions')
content = content.replace('class="text-primary-fixed hover:underline">Privacy Policy',
                          'class="text-primary-container font-semibold hover:underline hover:text-charcoal-black">Privacy Policy')

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)
