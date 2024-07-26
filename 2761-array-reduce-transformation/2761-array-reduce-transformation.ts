type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let output = init;
    for (const num of nums) {
        output = fn(output, num);
    }
    return output;
};