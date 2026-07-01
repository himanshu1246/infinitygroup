import re

def insert_videos(filepath, short_id, video_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    video_section = f"""
        <section class="py-16 px-margin-mobile md:px-margin-desktop bg-surface-ivory" data-aos="fade-up">
            <div class="max-w-container-max mx-auto text-center">
                <h2 class="font-headline-lg text-headline-lg text-charcoal-black mb-12" data-aos="flip-down">Project Videos</h2>
                <div class="flex flex-col md:flex-row gap-8 items-center justify-center">
                    <div class="w-full md:w-1/3 aspect-[9/16] rounded overflow-hidden shadow-lg border border-border-muted">
                        <iframe src="https://www.youtube.com/embed/{short_id}" class="w-full h-full" title="Project Short" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    </div>
                    <div class="w-full md:w-2/3 aspect-video rounded overflow-hidden shadow-lg border border-border-muted">
                        <iframe src="https://www.youtube.com/embed/{video_id}" class="w-full h-full" title="Project Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
        </section>

"""
    # Find the Project Gallery section and insert before it
    # <section class="py-16 px-margin-mobile md:px-margin-desktop bg-surface-container-lowest" data-aos="fade-up">
    #    <div class="max-w-container-max mx-auto text-center">
    #        <h2 class="font-headline-lg text-headline-lg text-charcoal-black mb-12" data-aos="flip-down">Project Gallery</h2>
    
    # We'll just replace the start of the gallery section with the video section + the start of the gallery section
    gallery_header = '<h2 class="font-headline-lg text-headline-lg text-charcoal-black mb-12" data-aos="flip-down">Project Gallery</h2>'
    # Find the section tag containing this
    
    # regex to find the section right before Project Gallery
    pattern = r'(<section[^>]*>\s*<div[^>]*>\s*<h2[^>]*>Project Gallery</h2>)'
    
    new_content = re.sub(pattern, video_section.replace('\\', '\\\\') + r'\1', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filepath}")

# Infinity Icon (Panvel)
# Short: WSS71np7kGA
# Video: -c38QdJuxnM
insert_videos('projects/infinity-icon-panvel.html', 'WSS71np7kGA', '-c38QdJuxnM')

# Infinity Ikon (Nerul)
# Short: e6-Kj0XukbY
# Video: u7x6bAhnTP4
insert_videos('projects/infinity-icon-nerul.html', 'e6-Kj0XukbY', 'u7x6bAhnTP4')

