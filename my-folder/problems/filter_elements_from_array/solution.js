/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const ret = [];
    arr.forEach((val, i) => {
        if (fn(val, i)) ret.push(val);
    })
    return ret;
};