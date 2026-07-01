import os
import glob
import re

def add_consent_checkbox():
    consent_html = """
<div class="mb-6 flex items-start text-left">
    <div class="flex items-center h-5 mt-0.5">
        <input id="consent" name="consent" type="checkbox" required class="w-4 h-4 border-border-muted rounded bg-surface-container-lowest focus:ring-2 focus:ring-primary-container cursor-pointer accent-primary-container">
    </div>
    <label for="consent" class="ml-3 font-body-sm text-body-sm text-on-surface-variant text-[12px] cursor-pointer leading-tight">
        I consent to receive RCS, WhatsApp, E-mail & SMS communications from <span class="font-bold text-charcoal-black">Infinity Group</span>. I also agree to the <a href="#" class="text-primary-fixed hover:underline">Terms & Conditions</a> and <a href="#" class="text-primary-fixed hover:underline">Privacy Policy</a>.
    </label>
</div>
"""
    
    files_to_check = [
        r'd:\infinity website\index.html',
        r'd:\infinity website\contact.html'
    ]
    files_to_check.extend(glob.glob(r'd:\infinity website\projects\*.html'))
    
    for filepath in files_to_check:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We need to insert the consent_html right before the submit button container.
        # In contact.html and projects/*.html, the button is direct child of the form or a container.
        # Let's just find the <button ... type="submit" and prepend the consent_html to it.
        # Wait, in index.html, it's inside <div class="pt-4 text-center">. We should prepend it before the button, or before the div.
        # The safest way is to prepend it right before the <button ... type="submit">.
        
        # Check if consent is already added
        if 'I consent to receive RCS' in content:
            continue
            
        # Using regex to find the button
        # Match <button ... type="submit"...> or <div class="pt-4 text-center">\s*<button...
        # It's easier to just do a simple replacement if we know the exact HTML, but they differ.
        
        # Let's replace <button with a function that prepends the consent HTML
        def replacer(match):
            return consent_html + match.group(0)
            
        new_content = re.sub(r'<button[^>]*type="submit"[^>]*>', replacer, content)
        
        # If it was in <div class="pt-4 text-center">, we might want to put the consent OUTSIDE that div to maintain left alignment.
        # Let's check if the button is preceded by <div class="pt-4 text-center">\s*
        def div_replacer(match):
            return consent_html + match.group(0)
            
        new_content2 = re.sub(r'<div class="pt-4 text-center">\s*<button[^>]*type="submit"[^>]*>', div_replacer, content)
        
        if '<div class="pt-4 text-center">' in content:
            content = new_content2
        else:
            content = new_content
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Added consent checkbox to all forms.")

add_consent_checkbox()
