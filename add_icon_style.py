import os
import re

dir_path = r'd:\infinity website'

style_block = """<style>
  .material-symbols-outlined {
    font-feature-settings: 'liga' !important;
    font-variant-ligatures: normal !important;
    text-transform: none !important;
    letter-spacing: normal !important;
  }
</style>
"""

count = 0
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if style block is already there
            if ".material-symbols-outlined {" not in content:
                # Insert right after the Material Symbols link
                pattern = re.compile(r'(<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined[^>]*>\s*)')
                
                if pattern.search(content):
                    new_content = pattern.sub(r'\g<1>' + style_block, content, count=1)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        print(f'Updated {filepath}')

print(f'Total files updated: {count}')
