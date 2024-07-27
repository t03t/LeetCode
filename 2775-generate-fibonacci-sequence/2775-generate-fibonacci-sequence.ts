function* fibGenerator(prev = 0, prev2 = 1): Generator<number, any, number> {
    yield prev;
    yield* fibGenerator(prev2, prev+prev2);
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */