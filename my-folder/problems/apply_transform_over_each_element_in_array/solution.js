/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const ret = []
    arr.forEach((val, i) => ret.push(fn(val, i)))
    return ret;
};