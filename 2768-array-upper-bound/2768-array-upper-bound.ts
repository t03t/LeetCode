interface Array<T> {
    upperBound(target: number): number;
}

Array.prototype.upperBound = function(target): number {
    let last_index = -1;
    for (let i = 0; i < this.length ; i++) {
        if (this[i] == target) {
            last_index = i;
        }
    }
    return last_index;
};

// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5