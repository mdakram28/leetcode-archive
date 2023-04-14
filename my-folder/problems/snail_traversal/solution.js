/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount*colsCount != this.length) return [];
    const rows = [...Array(rowsCount)].map(()=>[]);
    // console.log(rows);

    for(let i=0; i<this.length; i++) {
        let r = i%rowsCount;
        if (Math.floor(i/rowsCount)%2) r = rowsCount-r-1;
        // console.log(r);
        rows[r].push(this[i]);
    }
    return rows;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */