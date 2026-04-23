/**
 * EstateHub - Dark Mode Toggle Script
 * Persists user preference in localStorage
 * Works across all pages (web, admin, seller)
 */

(function () {
    'use strict';

    const STORAGE_KEY = 'estatehub_dark_mode';
    const DARK_CLASS = 'dark-mode';

    // Apply dark mode IMMEDIATELY on page load (before DOMContentLoaded)
    // to prevent flash of wrong theme
    function applyStoredTheme() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored === 'true') {
            document.documentElement.classList.add(DARK_CLASS);
        }
    }
    applyStoredTheme();

    // Toggle dark mode
    function toggleDarkMode() {
        const isDark = document.documentElement.classList.toggle(DARK_CLASS);
        localStorage.setItem(STORAGE_KEY, isDark ? 'true' : 'false');

        // Update all toggle buttons on the page
        updateToggleButtons(isDark);
    }

    // Update toggle button visual state
    function updateToggleButtons(isDark) {
        const buttons = document.querySelectorAll('.dark-mode-toggle');
        buttons.forEach(function (btn) {
            btn.setAttribute('title', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
            btn.setAttribute('aria-label', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
            btn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
        });
    }

    // Initialize toggle button(s) on DOMContentLoaded
    document.addEventListener('DOMContentLoaded', function () {
        const isDark = document.documentElement.classList.contains(DARK_CLASS);
        updateToggleButtons(isDark);

        // Attach click handlers to all toggle buttons
        document.querySelectorAll('.dark-mode-toggle').forEach(function (btn) {
            btn.addEventListener('click', toggleDarkMode);
        });
    });

    // Expose globally for inline usage if needed
    window.toggleDarkMode = toggleDarkMode;
})();
