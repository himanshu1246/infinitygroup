import os

base_dir = r'd:\infinity website'

html_files = []
# Find all HTML files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('class="text-primary-fixed hover:underline">Terms & Conditions',
                                      'class="text-charcoal-black font-bold hover:underline hover:text-primary-fixed">Terms & Conditions')
        new_content = new_content.replace('class="text-primary-fixed hover:underline">Privacy Policy',
                                          'class="text-charcoal-black font-bold hover:underline hover:text-primary-fixed">Privacy Policy')
                                          
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print('Done updating Enquire Now links.')
