/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let res = new Map();
    for (const obj of arr1) res.set(obj.id, obj);
    for (const obj of arr2) {
        if (!res.has(obj.id)) res.set(obj.id, obj);
        else {
            const prev = res.get(obj.id);
            for (const key of Object.keys(obj)) prev[key] = obj[key];
        }
    }
    const fin = new Array();
    for (let key of res.keys()) fin.push(res.get(key));
    return fin.sort((a,b) => a.id-b.id);
};