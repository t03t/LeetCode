function findWordsContaining(words: string[], x: string): number[] {
    let output = [];
    for (let i = 0; i < words.length; i++) {
        const word = words[i]
        if (word.includes(x)) {
            output.push(i);
        }
    }
    return output;
};