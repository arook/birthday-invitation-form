// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            let isValid = true;
            
            // Validate name
            const nameInput = document.querySelector('input[name="full_name"]');
            if (nameInput && nameInput.value.trim() === '') {
                showError(nameInput, 'Please enter your full name');
                isValid = false;
            } else if (nameInput) {
                clearError(nameInput);
            }
            
            // Validate email
            const emailInput = document.querySelector('input[name="email"]');
            if (emailInput) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (emailInput.value.trim() === '') {
                    showError(emailInput, 'Please enter your email address');
                    isValid = false;
                } else if (!emailPattern.test(emailInput.value.trim())) {
                    showError(emailInput, 'Please enter a valid email address');
                    isValid = false;
                } else {
                    clearError(emailInput);
                }
            }
            
            // Validate guests
            const attendingYes = document.querySelector('input[name="attending"][value="yes"]');
            const guestsInput = document.querySelector('input[name="guests"]');
            
            if (attendingYes && attendingYes.checked && guestsInput) {
                const guestsValue = parseInt(guestsInput.value, 10);
                if (isNaN(guestsValue) || guestsValue < 0) {
                    showError(guestsInput, 'Please enter a valid number of guests (0 or more)');
                    isValid = false;
                } else if (guestsValue > 5) {
                    showError(guestsInput, 'Maximum 5 additional guests allowed');
                    isValid = false;
                } else {
                    clearError(guestsInput);
                }
            }
            
            if (!isValid) {
                event.preventDefault();
            }
        });
    }
    
    // Show animated content
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.classList.add('fade-in');
    }
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Helper functions for form validation
function showError(inputElement, message) {
    // Remove existing error first if any
    clearError(inputElement);
    
    inputElement.classList.add('is-invalid');
    
    // Create error message element
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.innerText = message;
    
    // Insert after input
    inputElement.parentNode.appendChild(errorDiv);
}

function clearError(inputElement) {
    inputElement.classList.remove('is-invalid');
    
    // Find and remove any existing feedback elements
    const parent = inputElement.parentNode;
    const errorElements = parent.querySelectorAll('.invalid-feedback');
    errorElements.forEach(el => el.remove());
} 