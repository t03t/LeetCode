type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    if (arr.length < 1) {
        return [];
    }
    if (size > arr.length) {
        return [arr];
    }
    let chunked = [];
    let chunky = []
    let count = 0;
    for (let i = 0 ; i < arr.length ; i++) {
        const elem = arr[i];
        if (count < size) {
            count += 1;
            chunky.push(elem);
        }
        if ((count == size) || i == arr.length - 1) {
            chunked.push(chunky);
            count = 0;
            chunky = [];
        }
    }
    return chunked;
};
