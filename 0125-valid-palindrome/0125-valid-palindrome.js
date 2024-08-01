/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let word = (s.replaceAll(/[^0-9a-z]/gi, '').replaceAll(" ", "").toLowerCase());
    const length = word.length;
    if (length%2 === 0) {
        return word.slice(0, length/2) == word.slice(length/2, length).split("").reverse().join("");
    }
    return word.slice(0, length/2) == word.slice(length/2 + 1, length).split("").reverse().join("")
};