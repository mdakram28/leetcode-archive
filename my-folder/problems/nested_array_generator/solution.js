/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    for(const item of arr) {
        if (typeof item == 'object') {
            for (const item2 of inorderTraversal(item)) {
                yield item2;
            }
        } else {
            yield item;
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */