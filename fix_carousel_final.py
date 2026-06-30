import re

filepath = r"d:\infinity website\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change bg-cover to bg-contain md:bg-cover and add bg-no-repeat so it fits perfectly on mobile
content = content.replace('bg-cover bg-center opacity-100 md:opacity-70', 
                          'bg-contain md:bg-cover bg-center bg-no-repeat opacity-100 md:opacity-70')

# 2. Fix the arrows positioning on mobile (move them to the top half over the image)
content = content.replace('absolute left-4 top-1/2 transform -translate-y-1/2', 
                          'absolute left-4 top-[25%] md:top-1/2 transform -translate-y-1/2')

content = content.replace('absolute right-4 top-1/2 transform -translate-y-1/2', 
                          'absolute right-4 top-[25%] md:top-1/2 transform -translate-y-1/2')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI/UX and cropping fixed in index.html.")
