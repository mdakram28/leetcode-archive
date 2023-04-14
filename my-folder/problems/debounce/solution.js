/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let pending;
    return function(...args) {
        if (pending) clearTimeout(pending);
        pending = setTimeout(() => {
            pending = null;
            fn(...args);
        }, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */