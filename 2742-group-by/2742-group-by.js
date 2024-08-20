/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let res = {};
    for (let i of this) {
        let key = fn(i);
        if (res[key]) {
            res[key].push(i)
        }
        else {
            res[key] = [i]
        }
    }
    return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */