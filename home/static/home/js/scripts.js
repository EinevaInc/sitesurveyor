// Example: Add a simple hover effect to feature cards
document.addEventListener('DOMContentLoaded', function() {
    const featureCards = document.querySelectorAll('.feature-card');

    featureCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('shadow-lg'); // Add a larger shadow on hover
        });
        card.addEventListener('mouseleave', () => {
            card.classList.remove('shadow-lg');
        });
        const button = card.querySelector('.feature-button');
        button.addEventListener('click', () => {
             alert('Button clicked for: ' + card.querySelector('.card-title').textContent);
        });
    });
});