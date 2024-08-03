type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    const cache = new Map();
    return function(...args) {
        if (cache.has(fn)) {
            clearTimeout(cache.get(fn));
        }
        const timeoutId = setTimeout(() => fn(...args), t);
        cache.set(fn, timeoutId);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */