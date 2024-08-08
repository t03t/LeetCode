/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((res, rej) => {
        let c = 0;
        let results = new Array(functions.length);
        functions.forEach((fn, index) => {
            fn()
            .then((val) => {
                results[index] = val;
                c++;
                if (c === functions.length) {
                    res(results);
                }
            })
            .catch(err => rej(err));
        });
    });
};


/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */