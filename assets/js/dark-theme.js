// Dark Theme Toggle Script
(function() {
    'use strict';

    // Always set theme to light mode by default
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    // Remove theme toggle functionality
    setTimeout(function() {
        const toggleButton = document.querySelector('.theme-toggle');
        const themeIcon = toggleButton ? toggleButton.querySelector('.theme-icon') : null;
        if (themeIcon) {
            themeIcon.textContent = '🌙'; // Always show light mode icon
        }
        if (toggleButton) {
            toggleButton.disabled = true;
            toggleButton.style.opacity = 0.5;
            toggleButton.title = 'Theme switching disabled';
        }
    }, 100);
})();
