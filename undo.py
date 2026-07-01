with open('main.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="text-charcoal-black underline font-bold hover:text-primary-container">Terms & Conditions',
                          'class="text-primary-fixed hover:underline">Terms & Conditions')
content = content.replace('class="text-charcoal-black underline font-bold hover:text-primary-container">Privacy Policy',
                          'class="text-primary-fixed hover:underline">Privacy Policy')

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'r', encoding='utf-8') as f:
    content2 = f.read()

content2 = content2.replace('<div class="max-w-2xl mx-auto md:mt-20 bg-white/85 backdrop-blur-md p-6 md:p-8 rounded-2xl shadow-2xl border border-white/50 inline-block pointer-events-auto">',
                            '<div class="max-w-container-max mx-auto md:mt-20">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content2)

print('Undo complete.')
