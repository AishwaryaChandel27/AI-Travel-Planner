document.addEventListener('DOMContentLoaded', function() {
    const planForm = document.getElementById('planForm');
    const questionForm = document.getElementById('questionForm');
    const loading = document.getElementById('loading');
    const responseContainer = document.getElementById('responseContainer');
    const responseContent = document.getElementById('responseContent');

    // Handle travel plan form submission
    planForm.addEventListener('submit', function(e) {
        e.preventDefault();
        submitForm('/generate_plan', new FormData(planForm));
    });

    // Handle question form submission
    questionForm.addEventListener('submit', function(e) {
        e.preventDefault();
        submitForm('/ask_question', new FormData(questionForm));
    });

    function submitForm(url, formData) {
        // Show loading
        loading.style.display = 'block';
        responseContainer.style.display = 'none';

        // Clear any existing alerts
        clearAlerts();

        fetch(url, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            loading.style.display = 'none';

            if (data.success) {
                responseContent.textContent = data.response;
                responseContainer.style.display = 'block';

                // Scroll to response
                responseContainer.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'start' 
                });
            } else {
                showAlert('danger', data.error || 'An error occurred');
            }
        })
        .catch(error => {
            loading.style.display = 'none';
            console.error('Error:', error);
            showAlert('danger', 'Failed to connect to the server. Please try again.');
        });
    }

    function showAlert(type, message) {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

        document.querySelector('.container').insertBefore(alert, document.querySelector('.card'));

        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (alert.parentNode) {
                alert.remove();
            }
        }, 5000);
    }

    function clearAlerts() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => alert.remove());
    }
});

function clearResponse() {
    document.getElementById('responseContainer').style.display = 'none';
    document.getElementById('planForm').reset();
    document.getElementById('questionForm').reset();

    // Scroll back to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Utility functions
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Auto-hide after 5 seconds
    setTimeout(function() {
        alertDiv.remove();
    }, 5000);
}

function showLoadingState(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading-spinner"></span> Processing...';
    button.disabled = true;
    
    // Reset button after 10 seconds (fallback)
    setTimeout(function() {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 10000);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function createBudgetChart(canvas, data) {
    const ctx = canvas.getContext('2d');
    const labels = Object.keys(data);
    const values = Object.values(data);
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: [
                    '#007bff',
                    '#28a745',
                    '#ffc107',
                    '#dc3545',
                    '#17a2b8',
                    '#6c757d'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

// Progressive Web App features
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(function(registration) {
                console.log('ServiceWorker registration successful');
            })
            .catch(function(error) {
                console.log('ServiceWorker registration failed');
            });
    });
}

// Offline detection
window.addEventListener('online', function() {
    showAlert('You are back online!', 'success');
});

window.addEventListener('offline', function() {
    showAlert('You are offline. Some features may not work.', 'warning');
});

// Form auto-save (localStorage)
function autoSaveForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    const inputs = form.querySelectorAll('input, select, textarea');
    
    // Load saved data
    inputs.forEach(function(input) {
        const savedValue = localStorage.getItem(`autosave_${input.name}`);
        if (savedValue && input.type !== 'submit') {
            if (input.type === 'checkbox') {
                input.checked = savedValue === 'true';
            } else {
                input.value = savedValue;
            }
        }
    });
    
    // Save data on input
    inputs.forEach(function(input) {
        input.addEventListener('input', function() {
            if (input.type === 'checkbox') {
                localStorage.setItem(`autosave_${input.name}`, input.checked);
            } else {
                localStorage.setItem(`autosave_${input.name}`, input.value);
            }
        });
    });
    
    // Clear saved data on successful submit
    form.addEventListener('submit', function() {
        inputs.forEach(function(input) {
            localStorage.removeItem(`autosave_${input.name}`);
        });
    });
}

// Initialize auto-save for preferences form
autoSaveForm('preferencesForm');

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showAlert('Copied to clipboard!', 'success');
    }).catch(function() {
        showAlert('Failed to copy to clipboard.', 'danger');
    });
}

// Share functionality
function shareItinerary(url, title) {
    if (navigator.share) {
        navigator.share({
            title: title,
            url: url
        }).catch(function(error) {
            console.log('Error sharing:', error);
        });
    } else {
        copyToClipboard(url);
    }
}

// Print functionality
function printItinerary() {
    window.print();
}

// Export functionality
function exportItinerary(format) {
    // This would typically make an API call to generate the export
    showAlert(`Exporting itinerary as ${format}...`, 'info');
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl+S to save (prevent default and show save notification)
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        showAlert('Your preferences are automatically saved!', 'info');
    }
    
    // Escape to close modals
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal.show');
        modals.forEach(function(modal) {
            const bootstrapModal = bootstrap.Modal.getInstance(modal);
            if (bootstrapModal) {
                bootstrapModal.hide();
            }
        });
    }
});

// Accessibility improvements
function improveAccessibility() {
    // Add skip link
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link';
    skipLink.textContent = 'Skip to main content';
    skipLink.style.cssText = `
        position: absolute;
        top: -40px;
        left: 6px;
        background: var(--bs-primary);
        color: white;
        padding: 8px;
        text-decoration: none;
        z-index: 1000;
        border-radius: 4px;
    `;
    
    skipLink.addEventListener('focus', function() {
        this.style.top = '6px';
    });
    
    skipLink.addEventListener('blur', function() {
        this.style.top = '-40px';
    });
    
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Add main landmark
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.id = 'main-content';
    }
    
    // Enhance focus indicators
    const focusableElements = document.querySelectorAll('a, button, input, select, textarea, [tabindex]');
    focusableElements.forEach(function(element) {
        element.addEventListener('focus', function() {
            this.style.outline = '2px solid var(--bs-primary)';
            this.style.outlineOffset = '2px';
        });
        
        element.addEventListener('blur', function() {
            this.style.outline = '';
            this.style.outlineOffset = '';
        });
    });
}

// Initialize accessibility improvements
improveAccessibility();