with open('projects/infinity-township-rasayani.html', 'r', encoding='utf-8') as f:
    content = f.read()

images_to_add = """
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/WhatsApp%20Image%202026-07-01%20at%2013.56.35.jpeg" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/WhatsApp%20Image%202026-07-01%20at%2013.56.35%20(1).jpeg" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/WhatsApp%20Image%202026-07-01%20at%2013.56.35%20(2).jpeg" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/WhatsApp%20Image%202026-07-01%20at%2013.56.35%20(3).jpeg" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/WhatsApp%20Image%202026-07-01%20at%2013.56.35%20(4).jpeg" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
"""

# The last image we added previously was new 2.png
last_img = '<div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector(\'img\').src)"><img src="/projects/infinity%20heights%20gallery/new%202.png" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>'

content = content.replace(last_img, last_img + images_to_add)

with open('projects/infinity-township-rasayani.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added whatsapp images to gallery.')
