with open('projects/infinity-township-rasayani.html', 'r', encoding='utf-8') as f:
    content = f.read()

images_to_add = """
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/new.png" alt="Project Gallery Image" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/new%201.png" alt="Project Gallery Image" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/new%202.png" alt="Project Gallery Image" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
"""

# Wait, previously I used object-contain for the floor plans, but for regular photos object-cover is usually better. Let's stick with the existing class for consistency, which is object-contain. But if they are just regular photos, object-cover might look better in the grid.
# Actually I'll use object-contain as the existing ones use it.
images_to_add = """
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/new.png" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/new%201.png" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
                    <div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector('img').src)"><img src="/projects/infinity%20heights%20gallery/new%202.png" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>
"""


last_img = '<div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector(\'img\').src)"><img src="/projects/infinity%20heights%20gallery/2bhk%20unit%20in%20isometric.jpeg" alt="Project Gallery Image" class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110" loading="lazy" data-aos="zoom-in"></div>'

content = content.replace(last_img, last_img + images_to_add)

with open('projects/infinity-township-rasayani.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added new images to gallery.')
