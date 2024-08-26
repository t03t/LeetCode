/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let flatarr = [];
    for (let miniArr of arr) {
        if (Array.isArray(miniArr) && n > 0) {
            flatarr.push(...flat(miniArr, n - 1));
        }
        else {
            flatarr.push(miniArr);
        }
    }
    return flatarr;
};