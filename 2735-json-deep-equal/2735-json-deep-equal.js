/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    return Array.isArray(o1) && Array.isArray(o2) ? o1.length === o2.length && o1.every((n,i) => JSON.stringify(n).split('').sort().join('')===JSON.stringify(o2[i]).split('').sort().join('')) : JSON.stringify(o1).split('').sort().join('')
         === JSON.stringify(o2).split('').sort().join('')
};