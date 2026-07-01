import os

def mark_viviana_completed():
    # 1. Update projects/viviana-neral.html
    filepath = r'd:\infinity website\projects\viviana-neral.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The hero badge might have the garbled emoji or '🟡 ONGOING'
    # Let's replace 'ONGOING' with 'COMPLETED' inside the hero badge
    import re
    # Match the badge text inside the top-6 right-6 div
    content = re.sub(r'(<div class="absolute top-6 right-6 z-20">\s*<div[^>]*>)\s*[^<]*ONGOING\s*(</div>)', r'\1\n                    ✅ COMPLETED\n                \2', content)

    # Match the status card
    content = content.replace(
        '<div class="font-headline-md text-headline-md text-charcoal-black">Ongoing</div>',
        '<div class="font-headline-md text-headline-md text-charcoal-black">Completed</div>'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 2. Update projects.html
    filepath = r'd:\infinity website\projects.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the Viviana block and replace the badge
    # We can just look for the Viviana image and then the next ONGOING
    # Actually, let's just replace the specific badge HTML that has yellow-300
    # Wait, the other projects might also have ONGOING. We only want to change Viviana.
    
    viviana_start = content.find('<!-- Viviana -->')
    viviana_end = content.find('<!--', viviana_start + 10)
    if viviana_end == -1:
        viviana_end = len(content)
        
    viviana_block = content[viviana_start:viviana_end]
    
    new_viviana_block = re.sub(
        r'<span class="w-2 h-2 rounded-full bg-yellow-300 mr-2"></span>[^<]*ONGOING',
        '<span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span> ✅ COMPLETED',
        viviana_block
    )
    
    content = content[:viviana_start] + new_viviana_block + content[viviana_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 3. Update index.html
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace "Ready to Move" with "Completed" for Viviana
    content = content.replace(
        '<div class="absolute top-4 left-4 bg-charcoal-black text-on-primary px-2 py-1 font-label-caps text-label-caps tracking-widest uppercase rounded text-[10px]">Ready to Move</div>',
        '<div class="absolute top-4 left-4 bg-charcoal-black text-on-primary px-2 py-1 font-label-caps text-label-caps tracking-widest uppercase rounded text-[10px]">Completed</div>'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Marked Viviana as Completed everywhere.")

mark_viviana_completed()
