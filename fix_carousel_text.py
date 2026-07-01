with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a glassmorphism background to the text to ensure readability over the images
content = content.replace('<div class="max-w-container-max mx-auto md:mt-20">',
                          '<div class="max-w-2xl mx-auto md:mt-20 bg-white/85 backdrop-blur-md p-6 md:p-8 rounded-2xl shadow-2xl border border-white/50 inline-block pointer-events-auto">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
