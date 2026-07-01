with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace RERA for Infinity Ikon. 
# We need to make sure we only replace it for Infinity Ikon.
# We can search for the block of Infinity Ikon.
import re
# Since we know the exact string, we can do this:
# But other projects might also have [Pending]. 
# In projects.html, line 342 has "RERA: [Pending]". We can replace it in the context of Infinity Ikon.
content = re.sub(r'(<h3 class="font-headline-lg text-headline-lg text-primary-container mb-1">Infinity Ikon</h3>[\s\S]*?)RERA: \[Pending\]', r'\1RERA: P51700029339', content)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('projects/infinity-icon-nerul.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('[TO BE FILLED — add RERA number here]', 'P51700029339')

with open('projects/infinity-icon-nerul.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("RERA updated.")
