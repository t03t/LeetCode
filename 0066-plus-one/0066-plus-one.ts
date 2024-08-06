function plusOne(digits: number[]): number[] {
    // [1, 2, 9, 9]
    // [9, 9, 2, 1]
    // [0, 0, 3, 1]
    // [1, 3, 0, 0]
    let remainder = 1;
    let res = [];
    for (let digit of digits.reverse()) {
        digit += remainder;
        if (digit === 10) {
            res.push(0);
            remainder = 1;
        }
        else {
            res.push(digit);
            remainder = 0;
        }
    }
    if (remainder) {
        res.push(remainder);
    }
    return res.reverse();
};