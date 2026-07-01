import os

def fix_text_flow(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. We change the text container from absolute on all screens, to absolute ONLY on desktop.
    # We will search for: <div class="absolute inset-0 w-full flex flex-col justify-end pb-8 md:justify-center md:pb-0 z-10 text-center px-6">
    content = content.replace(
        '<div class="absolute inset-0 w-full flex flex-col justify-end pb-8 md:justify-center md:pb-0 z-10 text-center px-6">',
        '<div class="md:absolute md:inset-0 w-full flex flex-col justify-center py-6 md:py-0 md:justify-center z-10 text-center px-6">'
    )
    
    # Wait, in the previous script I changed the HTML to pb-8, but let's double check exact string.
    # In index.html it is currently:
    # <div class="absolute inset-0 w-full flex flex-col justify-end pb-8 md:justify-center md:pb-0 z-10 text-center px-6">
    # We will also add a little bit of margin-top so it's not completely flush with the image if we need it, but py-6 gives padding.

    # 2. We should also add mt-[80px] to the section or something?
    # No, the navbar is fixed. The image is at the very top, so the navbar overlaps the top of the image.
    # This is standard for full-screen hero headers. The user didn't complain about the image being under the navbar, they complained they couldn't see the text.
    # By moving the text below the image on mobile, it will be perfectly visible.

    # 3. For Slide 2 and 3 inactive state:
    # They are absolute inset-0. If the text is NOT absolute on mobile, an absolute inset-0 slide will not have its height dictated correctly?
    # Wait. Inactive slides have:
    # <div class="carousel-slide absolute inset-0 w-full h-full transition-opacity duration-1000 opacity-0 pointer-events-none z-0">
    # If the text is NOT absolute, it will flow below the image and push the height of the inactive slide? No, because the inactive slide is absolute inset-0, so its height is 100% of the parent. Its contents might overflow, but we have overflow-hidden.
    # Let's ensure it works smoothly.

    # Let's just restore the paragraph on mobile since we have plenty of space now!
    content = content.replace(
        'font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-8 md:mb-10 hidden md:block',
        'font-body-lg text-body-lg text-secondary-fixed/90 max-w-2xl mx-auto mb-6 md:mb-10'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed text flow")

fix_text_flow(r'd:\infinity website\index.html')
