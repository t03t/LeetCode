interface String {
    replicate(times: number): string;
}

String.prototype.replicate = function(times): string {
    let res = "";
    for (let i = 0; i < times ; i++ ) {
        res += this;
    }
    return res;
}