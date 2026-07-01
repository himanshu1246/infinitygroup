import os

def restore_state_two():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current classes (State 3: Crop)
    crop_classes = "md:w-full md:h-[85vh] md:object-cover"
    
    # The previous classes (State 2: Gaps)
    gap_classes = "md:max-w-full md:max-h-[85vh] md:w-auto md:mx-auto"
    
    # Replace them
    content = content.replace(crop_classes, gap_classes)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Restored State 2 (Gaps/Centered Layout)")

restore_state_two()
