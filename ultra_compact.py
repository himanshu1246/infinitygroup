import os

def compact_text_and_remove_gaps(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove pt-20 from main to kill the top gap
    content = content.replace(
        '<main class="flex-grow pt-20 md:pt-0">',
        '<main class="flex-grow">'
    )

    # 2. Make text incredibly compact on mobile so it fits under the navbar on short images
    # Replace the container padding
    content = content.replace(
        'justify-end pb-8 md:justify-center',
        'justify-end pb-3 md:justify-center'
    )
    
    # Replace the title size and margin
    content = content.replace(
        'font-display-lg text-[2rem] leading-none md:text-display-lg text-on-primary mb-2 md:mb-6',
        'font-display-lg text-[1.5rem] leading-none md:text-display-lg text-on-primary mb-1 md:mb-6'
    )
    
    # Replace the badge margin
    content = content.replace(
        'mb-2 md:mb-6 border border-primary-fixed/50',
        'mb-1 md:mb-6 border border-primary-fixed/50'
    )

    # Replace the button padding
    content = content.replace(
        'px-6 py-3 md:px-8 md:py-4',
        'px-4 py-2 md:px-8 md:py-4 text-[12px] md:text-label-caps'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed.")

compact_text_and_remove_gaps(r'd:\infinity website\index.html')
