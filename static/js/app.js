
document.addEventListener('DOMContentLoaded', function() {
    // Form elements
    const planForm = document.getElementById('planForm');
    const questionForm = document.getElementById('questionForm');
    const loading = document.getElementById('loading');
    const responseContainer = document.getElementById('responseContainer');
    const responseContent = document.getElementById('responseContent');

    // Enhanced loading animation
    function showLoading(message = 'Generating your personalized travel response...') {
        loading.style.display = 'block';
        loading.innerHTML = `
            <div class="loading-container">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <div class="loading-text">${message}</div>
                <div class="mt-2">
                    <small class="text-muted">This may take a few moments<span class="loading-dots"></span></small>
                </div>
            </div>
        `;
        responseContainer.style.display = 'none';
        
        // Smooth scroll to loading
        loading.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    function hideLoading() {
        loading.style.display = 'none';
    }

    // Enhanced response display
    function showResponse(response, title = 'AI Travel Recommendation') {
        hideLoading();
        
        responseContent.innerHTML = formatResponse(response);
        responseContainer.style.display = 'block';
        
        // Update header title
        const headerTitle = responseContainer.querySelector('.card-title');
        if (headerTitle) {
            headerTitle.innerHTML = `<i class="fas fa-robot me-2"></i>${title}`;
        }
        
        // Add animation class
        responseContainer.classList.add('animate-in');
        
        // Smooth scroll to response
        setTimeout(() => {
            responseContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    }

    // Format response text for better readability
    function formatResponse(text) {
        // Convert markdown-style formatting to HTML
        let formatted = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/### (.*?)$/gm, '<h5 class="mt-3 mb-2 text-primary">$1</h5>')
            .replace(/## (.*?)$/gm, '<h4 class="mt-4 mb-2 text-primary">$1</h4>')
            .replace(/# (.*?)$/gm, '<h3 class="mt-4 mb-3 text-primary">$1</h3>')
            .replace(/• (.*?)$/gm, '<li class="mb-1">$1</li>')
            .replace(/- (.*?)$/gm, '<li class="mb-1">$1</li>');

        // Wrap consecutive list items in ul tags
        formatted = formatted.replace(/(<li.*?<\/li>\s*)+/g, '<ul class="mb-3">$&</ul>');

        return formatted;
    }

    // Enhanced error handling
    function showError(message) {
        hideLoading();
        
        const errorHtml = `
            <div class="alert alert-danger" role="alert">
                <i class="fas fa-exclamation-triangle me-2"></i>
                <strong>Error:</strong> ${message}
            </div>
        `;
        
        responseContent.innerHTML = errorHtml;
        responseContainer.style.display = 'block';
        
        // Smooth scroll to error
        responseContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // Enhanced form validation
    function validateForm(form) {
        const required = form.querySelectorAll('[required]');
        let isValid = true;
        
        required.forEach(field => {
            if (!field.value.trim()) {
                field.classList.add('is-invalid');
                isValid = false;
                
                // Add error message
                if (!field.nextElementSibling || !field.nextElementSibling.classList.contains('invalid-feedback')) {
                    const errorDiv = document.createElement('div');
                    errorDiv.className = 'invalid-feedback';
                    errorDiv.textContent = 'This field is required';
                    field.parentNode.insertBefore(errorDiv, field.nextSibling);
                }
            } else {
                field.classList.remove('is-invalid');
                // Remove error message
                const errorDiv = field.nextElementSibling;
                if (errorDiv && errorDiv.classList.contains('invalid-feedback')) {
                    errorDiv.remove();
                }
            }
        });
        
        return isValid;
    }

    // Plan form submission
    if (planForm) {
        planForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            if (!validateForm(planForm)) {
                return;
            }
            
            const formData = new FormData(planForm);
            const destination = formData.get('destination');
            
            showLoading(`Creating a personalized travel plan for ${destination}...`);
            
            try {
                const response = await fetch('/generate_plan', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                
                if (data.success) {
                    showResponse(data.response, `Travel Plan for ${data.destination}`);
                } else {
                    showError(data.error || 'Failed to generate travel plan');
                }
                
            } catch (error) {
                console.error('Error generating plan:', error);
                showError('Unable to generate travel plan. Please check your connection and try again.');
            }
        });
    }

    // Question form submission
    if (questionForm) {
        questionForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            if (!validateForm(questionForm)) {
                return;
            }
            
            const formData = new FormData(questionForm);
            const question = formData.get('question');
            
            showLoading(`Finding the best answer for your question...`);
            
            try {
                const response = await fetch('/ask_question', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                
                if (data.success) {
                    showResponse(data.response, 'Travel Question Answer');
                } else {
                    showError(data.error || 'Failed to answer question');
                }
                
            } catch (error) {
                console.error('Error answering question:', error);
                showError('Unable to answer your question. Please check your connection and try again.');
            }
        });
    }

    // Clear response function
    window.clearResponse = function() {
        responseContainer.style.display = 'none';
        responseContent.innerHTML = '';
        
        // Clear form fields
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.reset();
            // Remove validation classes
            form.querySelectorAll('.is-invalid').forEach(field => {
                field.classList.remove('is-invalid');
            });
            form.querySelectorAll('.invalid-feedback').forEach(error => {
                error.remove();
            });
        });
        
        // Smooth scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    // Enhanced form interactions
    const inputs = document.querySelectorAll('.form-control');
    inputs.forEach(input => {
        // Add focus effects
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
        
        // Real-time validation
        input.addEventListener('input', function() {
            if (this.hasAttribute('required') && this.value.trim()) {
                this.classList.remove('is-invalid');
                const errorDiv = this.nextElementSibling;
                if (errorDiv && errorDiv.classList.contains('invalid-feedback')) {
                    errorDiv.remove();
                }
            }
        });
    });

    // Add button click effects
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Create ripple effect
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.className = 'ripple';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Add loading states to buttons
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.disabled = true;
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
            
            setTimeout(() => {
                this.disabled = false;
                this.innerHTML = originalText;
            }, 1000);
        });
    });

    // Add CSS for ripple effect
    const style = document.createElement('style');
    style.textContent = `
        .btn {
            position: relative;
            overflow: hidden;
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
        
        .focused {
            transform: scale(1.02);
            transition: transform 0.2s ease;
        }
        
        .animate-in {
            animation: fadeInUp 0.5s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
});
