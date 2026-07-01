import re

def reorganize_projects():
    filepath = r'd:\infinity website\projects.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Suncity
    suncity_start = content.find('<!-- Suncity -->')
    # Find the end of the Suncity card. It ends before <!-- Infinity Ikon -->
    suncity_end = content.find('<!-- Infinity Ikon -->')
    suncity_card = content[suncity_start:suncity_end].strip()
    
    # Extract Viviana
    viviana_start = content.find('<!-- Viviana -->')
    # Find the end of the Viviana card. It ends before </div>\n            </div>\n\n            <!-- UPCOMING PROJECTS -->
    viviana_end = content.find('</div>\n            </div>\n\n            <!-- UPCOMING PROJECTS -->')
    # It might end with a few </div> tags. Let's find the next HTML comment or UPCOMING PROJECTS
    upcoming_start = content.find('<!-- UPCOMING PROJECTS -->')
    
    # We need to find the exact end of Viviana card. 
    # A card div ends with </div>. We can use regex or just slice.
    # Viviana is the last card in the Ongoing section.
    viviana_card_raw = content[viviana_start:upcoming_start]
    # The raw string includes the closing tags of the grid and section.
    # Let's cleanly extract just the card div.
    # The card starts with <div class="bg-surface-container-lowest...
    # We can match from <!-- Viviana --> to the end of its outer div.
    # We know the card structure has exactly 3 closing </div> tags at the end of the card? Let's check.
    # <div class="bg-...">
    #   <div class="relative...">...</div>
    #   <div class="p-8...">...</div>
    # </div>
    # So the card is a single top-level div.
    # I'll just use a simple regex to capture the card block.
    
    suncity_match = re.search(r'<!-- Suncity -->\s*<div class="bg-surface-container-lowest.*?</a>\s*</div>\s*</div>', content, re.DOTALL)
    viviana_match = re.search(r'<!-- Viviana -->\s*<div class="bg-surface-container-lowest.*?</a>\s*</div>\s*</div>', content, re.DOTALL)
    
    if not suncity_match or not viviana_match:
        print("Could not find project cards.")
        return
        
    suncity_card = suncity_match.group(0)
    viviana_card = viviana_match.group(0)
    
    # Remove them from their original locations
    content = content.replace(suncity_card, '')
    content = content.replace(viviana_card, '')
    
    # Now create the Completed Projects section
    completed_section = f'''
            <!-- COMPLETED PROJECTS -->
            <div class="mb-16 mt-16">
                <h2 class="font-headline-lg text-headline-lg text-charcoal-black mb-8 uppercase tracking-widest" data-aos="flip-down">Completed Projects</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-start">
                    
                    {suncity_card}
                    
                    {viviana_card}
                    
                </div>
            </div>
    '''
    
    # Insert it after Upcoming Projects
    # Let's find the end of the max-w-container-max div that wraps all project sections.
    # Wait, the structure is:
    # <div class="max-w-container-max mx-auto">
    #   <!-- ONGOING PROJECTS --> ...
    #   <!-- UPCOMING PROJECTS --> ...
    # </div>
    
    # I can just insert the completed_section right before the final closing </div> of that container, OR after Upcoming Projects section.
    # Let's find the Upcoming Projects section.
    upcoming_str = '<!-- UPCOMING PROJECTS -->'
    upcoming_start_idx = content.find(upcoming_str)
    
    # Let's just put Completed Projects AFTER Upcoming Projects.
    # Find the end of the Upcoming Projects div block.
    # Upcoming Projects block starts at <!-- UPCOMING PROJECTS --> and ends at the closing </div> of its block.
    
    # A simpler way: we can append it to the end of the <div class="max-w-container-max mx-auto"> block which holds these sections.
    # The end of this block is before: </section> <!-- End of Portfolio Section -->
    # Actually, we can just look for the first </section> after UPCOMING PROJECTS.
    end_of_section = content.find('</section>', upcoming_start_idx)
    # The closing </div> for the container is right before </section>.
    # So we can insert completed_section right before </div>\n    </section>
    
    # Let's find the exact insertion point:
    insertion_point = content.rfind('</div>', upcoming_start_idx, end_of_section)
    
    new_content = content[:insertion_point] + completed_section + '\n' + content[insertion_point:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully reorganized projects.")

reorganize_projects()
