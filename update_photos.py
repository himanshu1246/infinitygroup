with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('/asset/infinity%20township.png', '/asset/infinity%20height.jpeg')
content = content.replace('/asset/infinity%20vandhan%20heights.png', '/asset/infinity.jpeg')

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('projects/infinity-township-rasayani.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero
content = content.replace('src="/asset/infinity%20township.png"', 'src="/asset/infinity%20height.jpeg"')

# Add old hero to gallery
gallery_item = '<div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector(\'img\').src)"><img src="/asset/infinity%20township.png" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>\n                    '
content = content.replace('<div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">\n                    <div', '<div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">\n                    ' + gallery_item + '<div')

with open('projects/infinity-township-rasayani.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('projects/infinity-vandhan-heights-kharghar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero
content = content.replace('src="/asset/infinity%20vandhan%20heights.png"', 'src="/asset/infinity.jpeg"')

# Replace first placeholder in gallery with old hero
placeholder = '<div class="h-64 bg-charcoal-black border border-primary-container flex items-center justify-center"><div class="text-primary-fixed font-label-caps tracking-widest uppercase">Project Render 1</div></div>'
gallery_item = '<div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector(\'img\').src)"><img src="/asset/infinity%20vandhan%20heights.png" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>'

content = content.replace(placeholder, gallery_item)

with open('projects/infinity-vandhan-heights-kharghar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated photos.')
