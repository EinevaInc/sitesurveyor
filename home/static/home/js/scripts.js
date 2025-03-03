// scripts.js

document.addEventListener('DOMContentLoaded', function() {

    // --- Feature Card Hover Effect and Click ---
    const featureCards = document.querySelectorAll('.feature-card');

    featureCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('shadow-lg');
        });
        card.addEventListener('mouseleave', () => {
            card.classList.remove('shadow-lg');
        });

        const button = card.querySelector('.feature-button');
        if (button) { // Check if the button exists (important!)
            button.addEventListener('click', (event) => {
                event.preventDefault(); // Prevent default link behavior
                alert('Button clicked for: ' + card.querySelector('.card-title').textContent);
                // Replace the alert with your desired action, e.g.,
                // window.location.href = '/your-feature-page';  // Redirect to a detail page
            });
        }
    });


    // --- Smooth Scrolling for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });



    // --- Feature Request Form ---

    const form = document.querySelector('form'); // Select the form

    if (form) { // Check if the form exists (only run on the feature request page)

        form.addEventListener('submit', function(event) {
            let isValid = true;

            // Basic Validation (Example - you can add more)
            const nameInput = form.querySelector('#id_name');  // Get form fields by ID
            const emailInput = form.querySelector('#id_email');
            const titleInput = form.querySelector('#id_feature_title');
            const descriptionInput = form.querySelector('#id_feature_description');
            const agreeCheckbox = form.querySelector('#id_agree_to_terms');

            // Clear previous errors
            clearErrors();


            if (nameInput && nameInput.value.trim() === '') {
                addError(nameInput, 'Please enter your name.');
                isValid = false;
            }

            if (emailInput && !isValidEmail(emailInput.value)) {
                addError(emailInput, 'Please enter a valid email address.');
                isValid = false;
            }
            if (titleInput && titleInput.value.trim() === '') {
                addError(titleInput, 'Please enter a title.');
                isValid = false;
            }
            if (descriptionInput && descriptionInput.value.trim() === '') {
                addError(descriptionInput, 'Please enter a description.');
                isValid = false;
            }
            if (agreeCheckbox && !agreeCheckbox.checked) {
                 addError(agreeCheckbox, 'You must agree to the terms and conditions.');
                 isValid = false;
            }

            if (!isValid) {
                event.preventDefault(); // Prevent form submission if invalid
            }
        });

        // Helper function to add an error message
        function addError(field, message) {
            const errorElement = document.createElement('div');
            errorElement.classList.add('errorlist'); // Use Django's errorlist class
            errorElement.textContent = message;

            // Insert the error message *after* the input field
            const parent = field.parentNode;
            if (field.nextSibling) {
                parent.insertBefore(errorElement, field.nextSibling);
            } else {
                parent.appendChild(errorElement);
            }
            field.classList.add('is-invalid'); // Add Bootstrap's is-invalid class
        }

        // Simple email validation (you can use a more robust regex)
        function isValidEmail(email) {
            return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
        }

        // Helper function to clear all errors
        function clearErrors() {
            const errorElements = form.querySelectorAll('.errorlist');
            errorElements.forEach(el => el.remove());

            const invalidInputs = form.querySelectorAll('.is-invalid');
            invalidInputs.forEach(input => input.classList.remove('is-invalid'));
        }

         // Remove error when start typing
        const formInputs = form.querySelectorAll('.form-control, .form-select, .form-check-input');
        formInputs.forEach(input => {
            input.addEventListener('input', () => {
                const errorElement = input.parentNode.querySelector('.errorlist');
                if(errorElement) {
                    errorElement.remove();
                    input.classList.remove('is-invalid');
                }
            });
        });

    } // End if (form)
});