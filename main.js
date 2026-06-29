document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const menuBtn = document.querySelector('button.md\\:hidden');
    const navMenu = document.querySelector('.hidden.md\\:flex');
    
    if (menuBtn && navMenu) {
        menuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('hidden');
            navMenu.classList.toggle('flex');
            navMenu.classList.toggle('flex-col');
            navMenu.classList.toggle('absolute');
            navMenu.classList.toggle('top-full');
            navMenu.classList.toggle('left-0');
            navMenu.classList.toggle('w-full');
            navMenu.classList.toggle('h-screen');
            navMenu.classList.toggle('bg-charcoal-black/95');
            navMenu.classList.toggle('backdrop-blur-xl');
            navMenu.classList.toggle('p-6');
            navMenu.classList.toggle('shadow-lg');
            navMenu.classList.toggle('gap-4');
        });
    }

    // 2. Lenis Smooth Scrolling (if Lenis is loaded globally)
    if (typeof Lenis !== 'undefined') {
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1,
            smoothTouch: false,
            touchMultiplier: 2,
            infinite: false,
        });

        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);
    }

    // 3. Lazy Loading CSS Background Images via IntersectionObserver
    const lazyBackgrounds = document.querySelectorAll('[data-bg]');
    
    if ('IntersectionObserver' in window) {
        const bgObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const bgUrl = el.getAttribute('data-bg');
                    if (bgUrl) {
                        el.style.backgroundImage = bgUrl;
                        el.removeAttribute('data-bg');
                    }
                    observer.unobserve(el);
                }
            });
        }, {
            rootMargin: '0px 0px 200px 0px'
        });

        lazyBackgrounds.forEach(bg => {
            bgObserver.observe(bg);
        });
    }

    // 4. Active Link Highlighting
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath || (currentPath === '/' && linkPath === '/index.html')) {
            link.classList.remove('text-secondary-fixed');
            link.classList.add('text-primary-fixed', 'border-b-2', 'border-primary-fixed', 'pb-1');
        }
    });

    // 5. Aggressive Lead Gen Popup
    if (!localStorage.getItem('enquiryFilled')) {
        const modalHTML = `
            <div id="lead-modal" class="fixed inset-0 z-[100] flex items-center justify-center bg-charcoal-black/80 backdrop-blur-sm hidden opacity-0 transition-opacity duration-300">
                <div class="bg-surface-container-lowest p-8 md:p-12 rounded-lg max-w-md w-full mx-4 shadow-2xl relative transform scale-95 transition-transform duration-300">
                    <button id="close-modal" class="absolute top-4 right-4 text-on-surface-variant hover:text-charcoal-black transition-colors">
                        <span class="material-symbols-outlined">close</span>
                    </button>
                    <h2 class="font-headline-md text-headline-md text-charcoal-black mb-2 text-center">Exclusive Access</h2>
                    <p class="font-body-md text-body-md text-on-surface-variant text-center mb-6">Enter your details to receive premium brochures and VIP offers directly from Infinity Group.</p>
                    
                    <form id="lead-form" class="space-y-6">
                        <div>
                            <input type="text" placeholder="Full Name" required class="w-full border-b border-border-muted py-2 bg-transparent focus:outline-none focus:border-primary-fixed font-body-md text-charcoal-black">
                        </div>
                        <div>
                            <input type="email" placeholder="Email Address" required class="w-full border-b border-border-muted py-2 bg-transparent focus:outline-none focus:border-primary-fixed font-body-md text-charcoal-black">
                        </div>
                        <div>
                            <input type="tel" pattern="[0-9]{10}" title="Please enter exactly 10 digits" placeholder="Phone Number (10 digits)" required class="w-full border-b border-border-muted py-2 bg-transparent focus:outline-none focus:border-primary-fixed font-body-md text-charcoal-black">
                        </div>
                        <button type="submit" class="w-full btn-primary py-4 font-label-caps text-label-caps tracking-widest uppercase rounded mt-4">
                            Submit Enquiry
                        </button>
                    </form>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('lead-modal');
        const modalInner = modal.querySelector('div');
        const closeBtn = document.getElementById('close-modal');
        const form = document.getElementById('lead-form');
        
        let popupInterval;
        
        const showModal = () => {
            if (!localStorage.getItem('enquiryFilled') && modal.classList.contains('hidden')) {
                modal.classList.remove('hidden');
                // Trigger reflow for animation
                void modal.offsetWidth;
                modal.classList.remove('opacity-0');
                modalInner.classList.remove('scale-95');
                modalInner.classList.add('scale-100');
            }
        };

        const hideModal = () => {
            modal.classList.add('opacity-0');
            modalInner.classList.remove('scale-100');
            modalInner.classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 300);
        };
        
        // Show after 10 seconds, then every 10 seconds
        popupInterval = setInterval(showModal, 10000);
        
        closeBtn.addEventListener('click', hideModal);
        
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const btn = form.querySelector('button');
            const originalText = btn.textContent;
            btn.textContent = "Sending...";
            
            const inputs = form.querySelectorAll('input');
            const data = {
                name: inputs[0].value,
                email: inputs[1].value,
                phone: inputs[2].value,
                source: "Website Pop-up Form",
                message: ""
            };
            
            fetch("https://script.google.com/macros/s/AKfycbzbxxqJkurxEB7CiXrCySYUvQQauWl-5wNNwyBmOMLLX3CjnnkZlkUjkmtnrEe6eVb1vw/exec", {
                method: 'POST',
                headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(data => {
                localStorage.setItem('enquiryFilled', 'true');
                clearInterval(popupInterval);
                
                btn.textContent = "Thank You!";
                btn.classList.add('bg-green-600', 'text-white', 'border-green-600');
                
                setTimeout(hideModal, 1500);
            })
            .catch(error => {
                console.error("Error:", error);
                btn.textContent = originalText;
                alert("Something went wrong. Please try again or contact us directly.");
            });
        });
    }
});
