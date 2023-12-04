type Fn<T> = () => Promise<T>

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
    return new Promise((res, err) => {
        const resolved: T[] = [];
        let totalDone = 0;
        let errored = false;

        for(const fni in functions) {
            functions[fni]()
                .then((ret: T) => {
                    resolved[fni] = ret;
                    totalDone++;
                    if (!errored && totalDone == functions.length) {
                        res(resolved);
                    }
                })
                .catch(e => {
                    if (!errored) {
                        errored = true;
                        err(e);
                    }
                });
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */

