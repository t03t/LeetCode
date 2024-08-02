class TimeLimitedCache {
    cache;
    
    constructor() {
        this.cache = new Map();
    }
    
    set(key: number, value: number, duration: number): boolean {
        let hadKey = this.cache.get(key);
        if (hadKey) {
            clearTimeout(hadKey.timeoutId);
        }
        const timeoutId = setTimeout(() => this.cache.delete(key), duration);
        this.cache.set(key, { value, timeoutId });
        return Boolean(hadKey);
    }
    
    get(key: number): number {
        if (this.cache.has(key)) {
            return this.cache.get(key).value;
        }
        else {
            return -1;
        }
    }
    
    count(): number {
        return this.cache.size;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */