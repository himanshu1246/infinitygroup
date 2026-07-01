import os

def fix_carousel_scroll():
    filepath = r'd:\infinity website\index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The existing code to replace
    old_code = """        function resetInterval() {
            clearInterval(slideInterval);
            slideInterval = setInterval(nextSlide, 5000);
        }

        slideInterval = setInterval(nextSlide, 5000);
    </script>"""

    new_code = """        let isCarouselVisible = true;

        function startInterval() {
            clearInterval(slideInterval);
            if (isCarouselVisible) {
                slideInterval = setInterval(nextSlide, 5000);
            }
        }

        function resetInterval() {
            startInterval();
        }

        // Intersection Observer to pause carousel when out of view
        const carouselObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                isCarouselVisible = entry.isIntersecting;
                if (isCarouselVisible) {
                    startInterval();
                } else {
                    clearInterval(slideInterval);
                }
            });
        }, { threshold: 0.05 });
        
        const heroCarouselElement = document.getElementById('hero-carousel');
        if (heroCarouselElement) {
            carouselObserver.observe(heroCarouselElement);
        } else {
            startInterval();
        }
    </script>"""

    if old_code in content:
        content = content.replace(old_code, new_code)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated carousel logic with IntersectionObserver.")
    else:
        print("Could not find the exact old code block. Here is what is present:")
        # Just to help debug if it fails
        script_start = content.rfind('function resetInterval()')
        script_end = content.find('</script>', script_start)
        print(content[script_start:script_end+9])

fix_carousel_scroll()
