type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => JSONValue

function partial(fn: Fn, args: JSONValue[]): Fn {
    
    return function(...restArgs) {
        for (let i = 0; i < args.length ; i++) {
            if (args[i] === "_") {
                args[i] = restArgs.shift();
            }
        }
        return fn(...args.concat(restArgs));
    }
};