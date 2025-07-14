document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const planForm = document.getElementById('planForm');
    const questionForm = document.getElementById('questionForm');
    const responseDiv = document.getElementById('aiResponse');
    const loadingDiv = document.getElementById('loading');

    // Show loading state
    function showLoading() {
        if (loadingDiv) {
            loadingDiv.style.display = 'block';
        }
        if (responseDiv) {
            responseDiv.style.display = 'none';
        }
    }

    // Hide loading state
    function hideLoading() {
        if (loadingDiv) {
            loadingDiv.style.display = 'none';
        }
    }

    // Display response
    function displayResponse(response, isError = false) {
        hideLoading();
        if (responseDiv) {
            responseDiv.style.display = 'block';
            responseDiv.innerHTML = `
                <div class="alert ${isError ? 'alert-danger' : 'alert-success'}" role="alert">
                    <h5 class="alert-heading">
                        <i class="fas ${isError ? 'fa-exclamation-circle' : 'fa-check-circle'} me-2"></i>
                        ${isError ? 'Error' : 'Travel Recommendation'}
                    </h5>
                    <div class="response-content">
                        ${formatResponse(response)}
                    </div>
                </div>
            `;

            // Scroll to response
            responseDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Format response text
    function formatResponse(text) {
        // Convert markdown-like formatting to HTML
        return text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/• (.*?)(\n|$)/g, '<li>$1</li>')
            .replace(/(\d+)\. (.*?)(\n|$)/g, '<li>$2</li>')
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>')
            .replace(/(<li>.*?<\/li>)/gs, '<ul>$1</ul>')
            .replace(/<\/ul><br><ul>/g, '')
            .replace(/^/, '<p>')
            .replace(/$/, '</p>');
    }

    // Handle travel plan form submission
    if (planForm) {
        planForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(planForm);
            const destination = formData.get('destination');

            if (!destination || destination.trim() === '') {
                displayResponse('Please enter a destination before generating a plan.', true);
                return;
            }

            showLoading();

            fetch('/generate_plan', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    displayResponse(data.response);
                } else {
                    displayResponse(data.error || 'Failed to generate travel plan.', true);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                displayResponse('Network error. Please check your connection and try again.', true);
            });
        });
    }

    // Handle question form submission
    if (questionForm) {
        questionForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(questionForm);
            const question = formData.get('question');

            if (!question || question.trim() === '') {
                displayResponse('Please enter a question before submitting.', true);
                return;
            }

            showLoading();

            fetch('/ask_question', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    displayResponse(data.response);
                } else {
                    displayResponse(data.error || 'Failed to answer question.', true);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                displayResponse('Network error. Please check your connection and try again.', true);
            });
        });
    }

    // Add example destination suggestions
    const destinationInput = document.getElementById('destination');
    if (destinationInput) {
        const suggestions = [
            'Paris, France', 'Tokyo, Japan', 'London, UK', 'New York, USA',
            'Rome, Italy', 'Bangkok, Thailand', 'Sydney, Australia', 'Cairo, Egypt'
        ];

        destinationInput.addEventListener('focus', function() {
            // You can add autocomplete functionality here
        });
    }

    // Add smooth scrolling to all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});