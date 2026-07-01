with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the pill text black
content = content.replace('border border-primary-container bg-white/70 text-primary-container font-label-caps',
                          'border border-charcoal-black bg-white/70 text-charcoal-black font-bold font-label-caps')

# Make the paragraph text black
content = content.replace('text-on-surface-variant max-w-2xl mx-auto mb-8 md:mb-10 hidden md:block drop-shadow-[0_0_8px_rgba(255,255,255,1)]',
                          'text-charcoal-black font-semibold max-w-2xl mx-auto mb-8 md:mb-10 hidden md:block drop-shadow-[0_0_8px_rgba(255,255,255,1)]')

# Just in case the drop-shadow wasn't there (if I replaced something incorrectly before)
content = content.replace('text-on-surface-variant max-w-2xl mx-auto mb-8 md:mb-10 hidden md:block',
                          'text-charcoal-black font-semibold max-w-2xl mx-auto mb-8 md:mb-10 hidden md:block drop-shadow-[0_0_8px_rgba(255,255,255,1)]')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('main.js', 'r', encoding='utf-8') as f:
    main_content = f.read()

# Make the modal links black
main_content = main_content.replace('class="text-primary-container font-semibold hover:underline hover:text-charcoal-black">Terms & Conditions',
                                    'class="text-charcoal-black font-bold hover:underline hover:text-primary-fixed">Terms & Conditions')
main_content = main_content.replace('class="text-primary-container font-semibold hover:underline hover:text-charcoal-black">Privacy Policy',
                                    'class="text-charcoal-black font-bold hover:underline hover:text-primary-fixed">Privacy Policy')

# Also handle if they are still text-primary-fixed (from the undo)
main_content = main_content.replace('class="text-primary-fixed hover:underline">Terms & Conditions',
                                    'class="text-charcoal-black font-bold hover:underline hover:text-primary-fixed">Terms & Conditions')
main_content = main_content.replace('class="text-primary-fixed hover:underline">Privacy Policy',
                                    'class="text-charcoal-black font-bold hover:underline hover:text-primary-fixed">Privacy Policy')


with open('main.js', 'w', encoding='utf-8') as f:
    f.write(main_content)
