with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Slide 1
old_img_1 = '<img src="/asset/infinity%20icon%20.png" class="w-full h-auto block md:h-[85vh] md:object-contain md:w-full" alt="Infinity Icon" />'
new_bg_1 = '<div class="hidden md:block absolute inset-0 bg-center bg-cover bg-no-repeat filter blur-3xl scale-110 opacity-40" style="background-image: url(\'/asset/infinity%20icon%20.png\');"></div>\n                '
new_img_1 = '<img src="/asset/infinity%20icon%20.png" class="relative z-10 w-full h-auto block md:h-[85vh] md:object-contain md:w-full drop-shadow-2xl" alt="Infinity Icon" />'
content = content.replace(old_img_1, new_bg_1 + new_img_1)

# Slide 2
old_img_2 = '<img src="/asset/viviana.png" class="w-full h-full object-cover block md:h-[85vh] md:object-contain md:w-full" alt="Viviana" />'
new_bg_2 = '<div class="hidden md:block absolute inset-0 bg-center bg-cover bg-no-repeat filter blur-3xl scale-110 opacity-40" style="background-image: url(\'/asset/viviana.png\');"></div>\n                '
new_img_2 = '<img src="/asset/viviana.png" class="relative z-10 w-full h-full object-cover block md:h-[85vh] md:object-contain md:w-full drop-shadow-2xl" alt="Viviana" />'
content = content.replace(old_img_2, new_bg_2 + new_img_2)

# Slide 3
old_img_3 = '<img src="/asset/infinity%20icon.png" class="w-full h-full object-cover block md:h-[85vh] md:object-contain md:w-full" alt="Infinity Ikon" />'
new_bg_3 = '<div class="hidden md:block absolute inset-0 bg-center bg-cover bg-no-repeat filter blur-3xl scale-110 opacity-40" style="background-image: url(\'/asset/infinity%20icon.png\');"></div>\n                '
new_img_3 = '<img src="/asset/infinity%20icon.png" class="relative z-10 w-full h-full object-cover block md:h-[85vh] md:object-contain md:w-full drop-shadow-2xl" alt="Infinity Ikon" />'
content = content.replace(old_img_3, new_bg_3 + new_img_3)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added blurred background to carousel slides.")
