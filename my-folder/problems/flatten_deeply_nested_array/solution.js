/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n, depth) {
    depth ||= 0;
    if (depth >= n) return arr;
    const ret = [];
    for (const item of arr) {
        if (Array.isArray(item)) ret.push(...flat(item, n, depth+1));
        else ret.push(item);
    }
    return ret;
};