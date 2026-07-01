import os

def fix_bento_grid():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add items-start to the main bento grid to prevent vertical stretching
    content = content.replace(
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-8">',
        '<div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-start">'
    )

    # 2. Fix the Left Card
    content = content.replace(
        '<div class="relative flex-grow overflow-hidden">',
        '<div class="relative overflow-hidden">'
    )
    # The inner wrapper needs h-auto instead of h-full
    content = content.replace(
        '<div class="relative w-full h-full overflow-hidden bg-charcoal-black group-hover:scale-105',
        '<div class="relative w-full h-auto overflow-hidden bg-charcoal-black group-hover:scale-105'
    )

    # 3. Fix the Right Cards (Infinity Ikon and Viviana)
    # Remove flex-1 from the cards so they don't stretch
    content = content.replace(
        '<div class="flex-1 group card-hover',
        '<div class="group card-hover'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed bento grid in index.html")

def fix_projects_grid():
    filepath = r'd:\infinity website\projects.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add items-start to grid containers to prevent card stretching
    content = content.replace(
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">',
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-start">'
    )
    
    # 2. Fix card image wrapper
    # It was: <div class="relative w-full h-auto overflow-hidden bg-charcoal-black">
    # Wait, earlier I did: 
    # '<div class="h-64 bg-charcoal-black relative overflow-hidden">' -> '<div class="relative w-full h-auto overflow-hidden bg-charcoal-black">'
    # Let's verify that's fine. If it's h-auto, it won't force a height. And with items-start, the card won't stretch.
    # What about the card itself?
    # <div class="bg-surface-container-lowest border border-border-muted/50 rounded overflow-hidden flex flex-col card-hover ambient-shadow"
    # That is fine. 
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed grids in projects.html")

fix_bento_grid()
fix_projects_grid()
