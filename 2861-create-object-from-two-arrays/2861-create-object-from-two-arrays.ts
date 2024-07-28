type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function createObject(keysArr: JSONValue[], valuesArr: JSONValue[]): Record<string, JSONValue> {
    let obj = {};
    for (let i = 0; i < keysArr.length; i++) {
        const key = String(keysArr[i]);
        const elem = valuesArr[i];
        if (!obj.hasOwnProperty(key)) {
            obj[key] = elem;
        }
    }
    return obj;

};