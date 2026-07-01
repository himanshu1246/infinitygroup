import os

def patch_text_containers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Reduce padding on mobile from pb-24 to pb-8
    content = content.replace(
        'justify-end pb-24 md:justify-center', 
        'justify-end pb-8 md:justify-center'
    )
    
    # 2. Make badge smaller margin on mobile
    content = content.replace(
        'mb-4 md:mb-6 border',
        'mb-2 md:mb-6 border'
    )
    # We will also make the text slightly smaller on mobile for badge
    content = content.replace(
        'text-primary-fixed font-label-caps text-label-caps tracking-widest',
        'text-primary-fixed font-label-caps text-[10px] md:text-label-caps tracking-widest'
    )
    
    # 3. Make Title smaller margin on mobile, and optionally smaller text size
    # text-display-lg is huge on mobile, let's use text-[2rem] md:text-display-lg
    content = content.replace(
        'font-display-lg text-display-lg text-on-primary mb-4 md:mb-6',
        'font-display-lg text-[2rem] leading-none md:text-display-lg text-on-primary mb-2 md:mb-6'
    )
    
    # 4. Hide paragraph on mobile to save vertical space!
    # Currently it is: <p class="font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-8 md:mb-10">
    content = content.replace(
        'font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-8 md:mb-10',
        'font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-8 md:mb-10 hidden md:block'
    )
    
    # 5. Make button padding smaller on mobile
    content = content.replace(
        'px-8 py-4 font-label-caps',
        'px-6 py-3 md:px-8 md:py-4 font-label-caps'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched text containers")

patch_text_containers(r'd:\infinity website\index.html')
