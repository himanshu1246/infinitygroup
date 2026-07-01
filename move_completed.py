import re

def move_completed_to_top():
    filepath = r'd:\infinity website\projects.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Completed Projects block
    completed_start = content.find('<!-- COMPLETED PROJECTS -->')
    if completed_start == -1:
        print("Could not find Completed Projects section.")
        return

    # Find where the Completed Projects section ends.
    # It currently sits at the bottom, right before the closing </div> of max-w-container-max
    # Or we can just find the end of its div block.
    # The structure is:
    # <!-- COMPLETED PROJECTS -->
    # <div class="mb-16 mt-16">
    # ...
    # </div>
    # </div> (closing of max-w-container-max)
    # Let's extract from COMPLETED PROJECTS up to the final closing </div> before </section>
    
    # A safer way to find the end: look for the next section tag or closing div
    end_of_completed = content.find('</section>', completed_start)
    # The block ends right before the closing </div> of the container which is right before </section>
    end_div = content.rfind('</div>', completed_start, end_of_completed)
    
    completed_block = content[completed_start:end_div]
    
    # Remove it from the current location
    content = content[:completed_start] + content[end_div:]
    
    # Now insert it before ONGOING PROJECTS
    ongoing_start = content.find('<!-- ONGOING PROJECTS -->')
    if ongoing_start == -1:
        print("Could not find Ongoing Projects section.")
        return
        
    # We should probably remove the "mt-16" from Completed Projects if it's at the very top,
    # and add it to Ongoing Projects?
    # Actually, Ongoing Projects has `<div class="mb-16">`. We can just make Completed have `<div class="mb-16">`.
    completed_block = completed_block.replace('<div class="mb-16 mt-16">', '<div class="mb-16">')
    
    content = content[:ongoing_start] + completed_block + '\n            ' + content[ongoing_start:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Moved Completed Projects to the top.")

move_completed_to_top()
