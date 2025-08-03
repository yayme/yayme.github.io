// Dark Theme Toggle Script
(function() {
    'use strict';

    // Check for saved theme preference or default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply the saved theme on page load
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    // Initialize theme toggle functionality
    function initThemeToggle() {
        const toggleButton = document.querySelector('.theme-toggle');
        const themeIcon = toggleButton.querySelector('.theme-icon');
        
        if (!toggleButton || !themeIcon) return;
        
        // Set initial icon
        themeIcon.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
        
        // Add click event listener
        toggleButton.addEventListener('click', function(e) {
            e.preventDefault();
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            // Update theme
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update button icon
            themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThemeToggle);
    } else {
        initThemeToggle();
    }
})();
