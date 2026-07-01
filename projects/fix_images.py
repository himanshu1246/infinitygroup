import os
import re

dir_path = r'd:\infinity website\projects'

count_gallery = 0
for file in os.listdir(dir_path):
    if file.endswith('.html'):
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"',
                                      'class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-110"')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count_gallery += 1

print(f'Gallery files updated: {count_gallery}')

hero_files = ['infinity-vandhan-heights-kharghar.html', 'infinity-icon-nerul.html']
for file in hero_files:
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = re.compile(r'(<img src="/asset/[^"]+"\s+class=")([^"]+)("\s+alt="Project Hero"\s*/>)')
    
    def repl(match):
        return match.group(1) + 'w-full h-auto max-h-[70vh] object-contain mx-auto block' + match.group(3)
        
    new_content = pattern.sub(repl, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Hero image updated for {file}')
