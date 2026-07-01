import os

def revert_desktop_classes():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current classes (which crop the image)
    current_classes = "md:w-full md:h-[85vh] md:object-cover"
    
    # We remove them entirely so the image behaves exactly like mobile (w-full h-auto)
    content = content.replace(f" {current_classes}", "")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Reverted to full-width auto-height on desktop.")

revert_desktop_classes()
