import os

def fix_carousel_z_indexes():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The gradient overlay currently has no z-index.
    content = content.replace(
        '<div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent"></div>',
        '<div class="absolute inset-0 z-20 bg-gradient-to-t from-charcoal-black via-charcoal-black/40 to-transparent pointer-events-none"></div>'
    )
    
    # The text container currently has z-10.
    content = content.replace(
        '<div class="absolute inset-0 w-full flex flex-col justify-end pb-8 md:justify-center md:pb-0 z-10 text-center px-6">',
        '<div class="absolute inset-0 w-full flex flex-col justify-end pb-8 md:justify-center md:pb-0 z-30 text-center px-6 pointer-events-none">'
    )
    
    # Also, we need to make sure the buttons inside the text container are clickable, since pointer-events-none disables clicking.
    # The links/buttons inside the text container:
    content = content.replace(
        'class="inline-block btn-primary',
        'class="inline-block btn-primary pointer-events-auto'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed z-indexes.")

fix_carousel_z_indexes()
