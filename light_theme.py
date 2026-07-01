import os
import glob
import re

def fix_light_theme_heroes():
    for filepath in glob.glob(r'd:\infinity website\projects\*.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the hero section
        main_match = re.search(r'<main[^>]*>', content)
        if not main_match:
            continue
            
        start_idx = content.find('<section', main_match.end())
        end_idx = content.find('</section>', start_idx) + len('</section>')
        
        hero_html = content[start_idx:end_idx]
        
        # We only want to apply this to the hero section we just stacked.
        
        # 1. Change section background
        hero_html = hero_html.replace('bg-charcoal-black', 'bg-surface-ivory')
        
        # 2. Remove the dark gradient overlay from the image wrapper
        hero_html = re.sub(r'<div class="absolute inset-0 bg-gradient-to-t from-charcoal-black via-transparent to-transparent opacity-80"></div>', '', hero_html)
        
        # 3. Change text colors
        # "Infinity Group... presents"
        hero_html = hero_html.replace('text-primary-fixed mb-4 uppercase', 'text-on-surface-variant mb-4 uppercase')
        
        # Main Title (Infinity Icon)
        hero_html = hero_html.replace('text-on-primary mb-2', 'text-charcoal-black mb-2')
        
        # Subtitle (at Shedung...)
        hero_html = hero_html.replace('text-secondary-fixed/90 max-w-2xl', 'text-on-surface-variant max-w-2xl')
        
        # Badges
        # Original: border border-primary-container/50 bg-charcoal-black/50 backdrop-blur-sm text-primary-fixed
        hero_html = hero_html.replace('border-primary-container/50 bg-surface-ivory/50 backdrop-blur-sm text-primary-fixed', 'border-border-muted bg-surface text-charcoal-black')
        hero_html = hero_html.replace('border-primary-container/50 bg-charcoal-black/50 backdrop-blur-sm text-primary-fixed', 'border-border-muted bg-surface text-charcoal-black')
        
        # MahaRERA
        hero_html = hero_html.replace('text-secondary-fixed/70 font-label-caps', 'text-on-surface-variant/70 font-label-caps')
        
        new_content = content[:start_idx] + hero_html + content[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Fixed theme in {os.path.basename(filepath)}")

fix_light_theme_heroes()
