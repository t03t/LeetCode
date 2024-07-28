type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    try {
        const [res1, res2] = await Promise.all([promise1, promise2]);
        return res1 + res2;
    } catch (e) {
        throw new Error(e);
    }
    
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */