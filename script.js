// Ensure DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {

    // =====================
    // Scroll animations for sections
    // =====================
    const sections = document.querySelectorAll('section');

    const revealSection = () => {
        sections.forEach(section => {
            const top = section.getBoundingClientRect().top;
            const trigger = window.innerHeight / 1.2;

            if (top < trigger) {
                section.classList.add('show');
            }
        });
    };

    window.addEventListener('scroll', revealSection);
    revealSection(); // run once on load

    // =====================
    // Mobile navigation toggle
    // =====================
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        hamburger.classList.toggle('open'); // optional: animate hamburger
    });

    // Optional: close menu when clicking a link
    const navLinks = document.querySelectorAll('.nav-menu li a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                hamburger.classList.remove('open');
            }
        });
    });

    // =====================
    // Contact form validation
    // =====================
    const contactForm = document.getElementById('contact-form');
    const formMsg = document.getElementById('form-msg');

    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        if (name === '' || email === '' || message === '') {
            formMsg.textContent = 'Please fill in all fields!';
            formMsg.style.color = 'red';
        } else {
            formMsg.textContent = 'Message sent successfully!';
            formMsg.style.color = 'lime';
            contactForm.reset();
        }
    });

    // =====================
    // Optional: simple fade-in animation for buttons
    // =====================
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            btn.style.transform = 'scale(1.1)';
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'scale(1)';
        });
    });

});
