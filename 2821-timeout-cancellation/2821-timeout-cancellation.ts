type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void
/**
## setTimeout()

A [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) to be executed after the timer expires.

The time, in milliseconds, that the timer should wait before the specified function or code is executed. If this parameter is omitted, a value of 0 is used, meaning execute "immediately", or more accurately, the next event cycle.

(The actual delay *may* be longer.)

### parameter:

delay : a number in milliseconds.

### return value:

timeoutID

## clearTimeout()

A timeout can be cleared using clearTimeout().

### parameter:

timeoutID:  identifier of the timeout you want to cancel. The corresponding call to `setTimeout()` returned this ID.
 */
function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
    const runningTimer = setTimeout(() => {
        fn(...args)
    }, t);
    function cancelFn() {
        clearTimeout(runningTimer);
    }
    return cancelFn;
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */