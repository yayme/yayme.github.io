// Dark Theme Toggle Script
(function() {
    'use strict';

    // Check for saved theme preference or default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply the saved theme on page load
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    // Initialize theme toggle functionality
    function initThemeToggle() {
        // Wait a bit for the DOM to be fully ready
        setTimeout(function() {
            const toggleButton = document.querySelector('.theme-toggle');
            const themeIcon = toggleButton ? toggleButton.querySelector('.theme-icon') : null;
            
            if (!toggleButton || !themeIcon) {
                console.log('Theme toggle button not found, retrying...');
                // Retry in case the button isn't loaded yet
                setTimeout(initThemeToggle, 500);
                return;
            }
            
            console.log('Theme toggle initialized');
            
            // Set initial icon
            themeIcon.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
            
            // Add click event listener
            toggleButton.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                const currentTheme = document.documentElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                
                console.log('Theme switching from', currentTheme, 'to', newTheme);
                
                // Update theme
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                
                // Update button icon
                themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
            });
        }, 100);
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThemeToggle);
    } else {
        initThemeToggle();
    }
})();
