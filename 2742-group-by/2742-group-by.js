/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let graph = new Map();

    for (let i of this) {
        let key = fn(i);
        if (graph.has(key)) {
            graph.get(key).push(i);
        }
        else {
            graph.set(key, [i]);
        }
    }

    let res = {};
    for (let [key, val] of graph.entries()) {
        res[key] = val;
    }
    return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */