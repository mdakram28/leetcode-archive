/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const groups = {};
    for (const item of this) {
        const group = fn(item);
        groups[group] ||= [];
        groups[group].push(item);
    }
    return groups;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */