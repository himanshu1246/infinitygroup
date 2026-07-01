import os
import re

base_dir = r'd:\infinity website'

# 1. Create thank-you.html
about_path = os.path.join(base_dir, 'about.html')
thank_you_path = os.path.join(base_dir, 'thank-you.html')

with open(about_path, 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract parts before <main class="flex-grow"> and after </main>
main_start = about_content.find('<main class="flex-grow">')
main_end = about_content.find('</main>') + len('</main>')

head_nav = about_content[:main_start]
# We'll fix the title and description
head_nav = head_nav.replace('<title>About Us - Infinity Developers</title>', '<title>Thank You - Infinity Developers</title>')
head_nav = head_nav.replace('content="Learn about Infinity Developers, our 15+ years of excellence, and our core philosophy."', 'content="Thank you for your enquiry. We will get back to you shortly."')
head_nav = head_nav.replace('content="About Us - Infinity Developers"', 'content="Thank You - Infinity Developers"')

footer_etc = about_content[main_end:]

thank_you_main = """<main class="flex-grow flex items-center justify-center">
    <section class="w-full flex items-center justify-center py-24 md:py-32 bg-surface-ivory">
        <div class="max-w-2xl text-center px-4" data-aos="fade-up">
            <span class="material-symbols-outlined text-[64px] text-primary-fixed mb-6" style="font-variation-settings: 'FILL' 1;">check_circle</span>
            <h1 class="font-display-lg text-display-lg text-charcoal-black mb-6">Thank You!</h1>
            <p class="font-body-lg text-body-lg text-on-surface-variant mb-10">
                We have successfully received your enquiry. Our team will review your request and get back to you shortly.
            </p>
            <a href="/index.html" class="inline-block btn-primary px-8 py-4 font-label-caps text-label-caps tracking-widest uppercase rounded">
                Return to Home
            </a>
        </div>
    </section>
</main>"""

with open(thank_you_path, 'w', encoding='utf-8') as f:
    f.write(head_nav + thank_you_main + footer_etc)

print("Created thank-you.html")

# 2. Modify main.js
main_js_path = os.path.join(base_dir, 'main.js')
with open(main_js_path, 'r', encoding='utf-8') as f:
    main_js_content = f.read()

# Replace the specific block in main.js
old_js_block = """            .then(data => {
                localStorage.setItem('enquiryFilled', 'true');
                clearInterval(popupInterval);
                
                btn.textContent = "Thank You!";
                btn.classList.add('bg-green-600', 'text-white', 'border-green-600');
                
                setTimeout(hideModal, 1500);
            })"""

new_js_block = """            .then(data => {
                localStorage.setItem('enquiryFilled', 'true');
                clearInterval(popupInterval);
                window.location.href = '/thank-you.html';
            })"""

if old_js_block in main_js_content:
    main_js_content = main_js_content.replace(old_js_block, new_js_block)
    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(main_js_content)
    print("Updated main.js")
else:
    print("Could not find the old block in main.js")


# 3. Modify contact.html
contact_path = os.path.join(base_dir, 'contact.html')
with open(contact_path, 'r', encoding='utf-8') as f:
    contact_content = f.read()

old_contact_block = """            .then(data => {
                if (btn) {
                    btn.textContent = "Message Sent Successfully!";
                    btn.classList.add('bg-green-600', 'text-white', 'border-green-600');
                    setTimeout(() => { btn.textContent = originalText; btn.classList.remove('bg-green-600', 'text-white', 'border-green-600'); }, 3000);
                }
                contactForm.reset();
            })"""

new_contact_block = """            .then(data => {
                window.location.href = '/thank-you.html';
            })"""

if old_contact_block in contact_content:
    contact_content = contact_content.replace(old_contact_block, new_contact_block)
    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(contact_content)
    print("Updated contact.html")
else:
    print("Could not find the old block in contact.html")

