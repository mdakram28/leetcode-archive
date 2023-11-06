/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    var retObj = {};

    for(const item of arr1) {
        retObj[item.id] = item;
    }

    for(const item of arr2) {
        const id = item.id;
        if (retObj[id])
        {
            Object.assign(retObj[id], item);
        }
        else
        {
            retObj[id] = item;
        }
    }

    return Object.values(retObj).sort((a, b) => a.id - b.id);
    // return Object.values(retObj);
};