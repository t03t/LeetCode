/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) {
        return "null";
    }
    
    if (typeof object === "string") {
        return `"${object}"`;
    }
    
    if (typeof object === "number" || typeof object === "boolean") {
        return String(object);
    }

    if (Array.isArray(object)) {
        const elements = object.map(element => jsonStringify(element));
        return `[${elements.join(",")}]`;
    }

    if (typeof object === "object") {
        const keys = Object.keys(object);
        const keyValuePairs = keys.map(key => {
            const value = jsonStringify(object[key]);
            return `"${key}":${value}`;
        });
        return `{${keyValuePairs.join(",")}}`;
    }
    
    // If the input is not recognized, return undefined.
    return undefined;
};