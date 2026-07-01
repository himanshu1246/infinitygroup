import os

files_to_update = [
    'd:\\infinity website\\projects\\infinity-icon-nerul.html',
    'd:\\infinity website\\projects\\infinity-icon-panvel.html',
    'd:\\infinity website\\projects\\infinity-township-rasayani.html'
]

modal_code = """
<!-- Gallery Modal -->
<div id="gallery-modal" class="fixed inset-0 z-[100] bg-charcoal-black/95 hidden flex items-center justify-center p-4 transition-opacity duration-300" onclick="closeGalleryModal()">
    <span class="absolute top-6 right-6 text-white cursor-pointer material-symbols-outlined text-[32px] hover:text-primary-container transition-colors">close</span>
    <img id="modal-img" src="" class="max-w-full max-h-full object-contain" onclick="event.stopPropagation()">
</div>
<script>
    function openGalleryModal(src) {
        document.getElementById('modal-img').src = src;
        document.getElementById('gallery-modal').classList.remove('hidden');
    }
    function closeGalleryModal() {
        document.getElementById('gallery-modal').classList.add('hidden');
        document.getElementById('modal-img').src = '';
    }
</script>
</body>
"""

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update grid cols
    content = content.replace('<div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6">',
                              '<div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">')
                              
    # 2. Update gallery container (remove h-64 on mobile, add cursor-pointer and onclick)
    content = content.replace('<div class="h-64 border border-primary-container overflow-hidden group">',
                              '<div class="w-full h-auto md:h-64 border border-primary-container overflow-hidden group cursor-pointer" onclick="openGalleryModal(this.querySelector(\'img\').src)">')

    # 3. Add modal code before </body> if not already there
    if 'id="gallery-modal"' not in content:
        content = content.replace('</body>', modal_code)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully updated gallery modal and grid in project files.")
