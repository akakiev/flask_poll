document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    // Fade-in effect for survey options
    const options = document.querySelectorAll('form input[type="radio"] + label');
    console.log('Options:', options);

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log('Fading in:', entry.target);
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    options.forEach(option => {
        observer.observe(option);
    });

    // Button animation on click
    const voteButton = document.querySelector('form button[type="submit"]');
    if (voteButton) {
        voteButton.addEventListener('click', function() {
            console.log('Button clicked');
            voteButton.classList.add('button-clicked');
            setTimeout(() => voteButton.classList.remove('button-clicked'), 150);
        });
    }
});
