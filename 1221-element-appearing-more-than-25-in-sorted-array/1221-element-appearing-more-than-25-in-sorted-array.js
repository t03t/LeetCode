/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    const quarter = Math.floor(arr.length/4);
    let counts = new Map();
    if (arr.length == 1) {
        return arr[0];
    }
    for (num of arr) {
        if (counts.get(num)) {
            const prev = counts.get(num);
            counts.set(num, prev+1);
            if (counts.get(num) > quarter) {
                return num;
            }
        }
        else {
            counts.set(num, 1);
        }
    }

};