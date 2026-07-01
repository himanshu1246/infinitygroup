import os

def append_consent_logic():
    filepath = r'd:\infinity website\main.js'
    
    # We will append an IIFE that adds the event listeners to all forms
    # We wait for DOMContentLoaded, or execute immediately if already loaded
    logic = """
// Add consent checkbox logic
(function() {
    function initConsentLogic() {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            const consentCheckbox = form.querySelector('input[name="consent"]');
            const submitBtn = form.querySelector('button[type="submit"]');
            
            if (consentCheckbox && submitBtn) {
                // Initial state
                submitBtn.disabled = !consentCheckbox.checked;
                if (submitBtn.disabled) {
                    submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
                } else {
                    submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
                }
                
                // On change
                consentCheckbox.addEventListener('change', (e) => {
                    submitBtn.disabled = !e.target.checked;
                    if (submitBtn.disabled) {
                        submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
                    } else {
                        submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
                    }
                });
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initConsentLogic);
    } else {
        initConsentLogic();
    }
})();
"""
    
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write('\n' + logic)
        
    print("Appended consent logic to main.js")

append_consent_logic()
