/**
 * EstateHub — CSRF Helper for jQuery AJAX
 * =========================================
 * This script automatically attaches the CSRF token to all jQuery AJAX
 * requests that modify data (POST, PUT, DELETE, PATCH).
 *
 * Include this file AFTER jQuery in any template that makes AJAX calls.
 *
 * SECURITY: This is a safety net — even if a developer forgets to manually
 * append csrfmiddlewaretoken to FormData, the token is still sent via header.
 */

(function() {
    'use strict';

    /**
     * Extract a cookie value by name.
     * Django sets the CSRF token in a cookie named 'csrftoken'.
     */
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    /**
     * Check if a given HTTP method is "safe" (does not modify data).
     * Safe methods do not need CSRF protection.
     */
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/i.test(method));
    }

    /**
     * Auto-configure jQuery to send CSRF token with all unsafe AJAX requests.
     */
    if (typeof $ !== 'undefined' && $.ajaxSetup) {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    var csrfToken = getCookie('csrftoken');
                    if (csrfToken) {
                        xhr.setRequestHeader("X-CSRFToken", csrfToken);
                    }
                }
            }
        });
    }

    // Make getCookie globally available for manual use
    window.getCSRFToken = function() {
        return getCookie('csrftoken');
    };
})();
