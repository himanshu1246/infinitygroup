import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pill_class = 'inline-block px-4 py-1 mb-2 md:mb-6 border border-charcoal-black bg-white/70 text-charcoal-black font-bold font-label-caps text-[10px] md:text-label-caps tracking-widest uppercase rounded-full backdrop-blur-sm'

# Slide 1 (Infinity Icon - Ongoing)
content = re.sub(
    r'(<span class=\"' + re.escape(pill_class) + r'\">)Featured Project(</span>\s*<h1[^>]*>Infinity Icon</h1>)',
    r'\g<1>🟡 ONGOING\g<2>', content
)

# Slide 2 (Viviana - Completed)
content = re.sub(
    r'(<span class=\"' + re.escape(pill_class) + r'\">)Featured Project(</span>\s*<h1[^>]*>Viviana</h1>)',
    r'\g<1>✅ COMPLETED\g<2>', content
)

# Slide 3 (Infinity Ikon - Ongoing)
content = re.sub(
    r'(<span class=\"' + re.escape(pill_class) + r'\">)Featured Project(</span>\s*<h1[^>]*>Infinity Ikon</h1>)',
    r'\g<1>🟡 ONGOING\g<2>', content
)

# Bento Grid Updates
content = content.replace(
    '<div class="absolute top-6 left-6 bg-charcoal-black text-on-primary px-3 py-1 font-label-caps text-label-caps tracking-widest uppercase rounded">On-Going</div>',
    '<div class="absolute top-6 left-6 bg-primary-container text-on-primary px-4 py-2 rounded-full font-label-caps text-label-caps tracking-widest uppercase flex items-center shadow-lg">🟡 ONGOING</div>'
)

content = content.replace(
    '<div class="absolute top-4 left-4 bg-charcoal-black text-on-primary px-2 py-1 font-label-caps text-label-caps tracking-widest uppercase rounded text-[10px]">Completed</div>',
    '<div class="absolute top-4 left-4 bg-primary-container text-on-primary px-4 py-2 rounded-full font-label-caps text-label-caps tracking-widest uppercase flex items-center shadow-lg text-[10px]">✅ COMPLETED</div>'
)

ikon_badge = '<div class="absolute top-4 left-4 z-10 bg-primary-container text-on-primary px-4 py-2 rounded-full font-label-caps text-label-caps tracking-widest uppercase flex items-center shadow-lg text-[10px]">🟡 ONGOING</div>'
content = content.replace(
    '<div class="relative overflow-hidden">\n<div class="relative w-full h-auto overflow-hidden bg-charcoal-black group-hover:scale-105 transform transition-transform duration-700" data-alt="A detailed view of the Infinity Icon residential project',
    '<div class="relative overflow-hidden">\n' + ikon_badge + '\n<div class="relative w-full h-auto overflow-hidden bg-charcoal-black group-hover:scale-105 transform transition-transform duration-700" data-alt="A detailed view of the Infinity Icon residential project'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Badges updated.')
