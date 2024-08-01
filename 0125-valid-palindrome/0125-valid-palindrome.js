/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let word = (s.replaceAll(/[^0-9a-z]/gi, '').replaceAll(" ", "").toLowerCase());
    let length = word.length;
    console.log(length);
    console.log(word.slice(0, length));
    console.log(word.slice(0, length/2));
    console.log(word.slice(length/2 +1, length).split("").reverse().join(""));
    if (length%2 === 0) {
        console.log("even")
        return word.slice(0, length/2) == word.slice(length/2, length).split("").reverse().join("");
    }
    return word.slice(0, length/2) == word.slice(length/2 + 1, length).split("").reverse().join("")
};