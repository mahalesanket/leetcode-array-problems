var TimeLimitedCache = function() {
    this.cache = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = Date.now();

    let exists = false;

    if (this.cache.has(key)) {
        const oldData = this.cache.get(key);

        if (oldData.expiry > currentTime) {
            exists = true;
        }
    }

    this.cache.set(key, {
        value: value,
        expiry: currentTime + duration
    });

    return exists;
};

/**
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    const currentTime = Date.now();

    if (!this.cache.has(key)) {
        return -1;
    }

    const data = this.cache.get(key);

    if (data.expiry <= currentTime) {
        this.cache.delete(key);
        return -1;
    }

    return data.value;
};

/**
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    const currentTime = Date.now();
    let count = 0;

    for (const [key, data] of this.cache) {
        if (data.expiry > currentTime) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }

    return count;
};