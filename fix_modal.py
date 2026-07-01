import os

def fix_modal_consent():
    filepath = r'd:\infinity website\main.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    consent_html = """                        <div class="mb-6 flex items-start text-left">
                            <div class="flex items-center h-5 mt-0.5">
                                <input id="consent_modal" name="consent" type="checkbox" required class="w-4 h-4 border-border-muted rounded bg-surface-container-lowest focus:ring-2 focus:ring-primary-container cursor-pointer accent-primary-container">
                            </div>
                            <label for="consent_modal" class="ml-3 font-body-sm text-body-sm text-on-surface-variant text-[12px] cursor-pointer leading-tight">
                                I consent to receive RCS, WhatsApp, E-mail & SMS communications from <span class="font-bold text-charcoal-black">Infinity Group</span>. I also agree to the <a href="#" class="text-primary-fixed hover:underline">Terms & Conditions</a> and <a href="#" class="text-primary-fixed hover:underline">Privacy Policy</a>.
                            </label>
                        </div>
"""
    
    # We find the button in main.js
    button_html = '<button type="submit" class="w-full btn-primary py-4 font-label-caps text-label-caps tracking-widest uppercase rounded mt-4">'
    
    if button_html in content and consent_html.strip() not in content:
        content = content.replace(button_html, consent_html + '                        ' + button_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Added consent checkbox to the modal in main.js")
    else:
        print("Could not find button or already added.")

fix_modal_consent()
