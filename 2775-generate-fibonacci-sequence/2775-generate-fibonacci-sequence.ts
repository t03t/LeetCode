function* fibGenerator(): Generator<number, any, number> {
    let prev = 0;
    let prev2 = 1;
    while(true) {
        yield prev;
        [prev, prev2] = [prev2, prev+prev2]
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */