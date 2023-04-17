var TimeLimitedCache = function() {
    this.cache = {};
    this.length = 0;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let ret = false;
    if (key in this.cache) {
        ret = true;
        clearTimeout(this.cache[key].ttl);
    } else {
        this.length++;
    }

    this.cache[key] = {
        value,
        ttl: setTimeout(() => {
            delete this.cache[key];
            this.length--;
        }, duration)
    };
    return ret;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return key in this.cache ? this.cache[key].value : -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.length;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */