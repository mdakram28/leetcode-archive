/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = function(functions, n) {
    return new Promise((res, rej) => {
        n = Math.min(n, functions.length);
        if (n==0) return res();
        let scheduled = 0;
        let resolved = 0;
        
        function scheduleOne() {
            functions[scheduled++]().then(() => {
                if (scheduled < functions.length) scheduleOne();
                resolved++;
                if(resolved == functions.length) {
                    res();
                }
            });
        }

        while(scheduled < n) {
            scheduleOne();
        }
    });
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */