import os
import re

dir_path = r'd:\infinity website'

new_link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />'

count = 0
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pattern = re.compile(r'<link[^>]*?family=Material\+Symbols\+Outlined[^>]*?>', re.IGNORECASE)
            
            if pattern.search(content):
                def repl(match, state={'count': 0}):
                    state['count'] += 1
                    if state['count'] == 1:
                        return new_link
                    return ''
                
                # We need to reset state count for each file
                class Replacer:
                    def __init__(self):
                        self.count = 0
                    def __call__(self, match):
                        self.count += 1
                        if self.count == 1:
                            return new_link
                        return ''
                
                new_content = pattern.sub(Replacer(), content)
                
                # Fix any escaped quotes in style
                new_content = new_content.replace(r"\'FILL\'", "'FILL'")
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
                    print(f'Updated {filepath}')

print(f'Total files updated: {count}')
