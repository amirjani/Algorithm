function sumOfTwo(a, b, v) {
    var set = new Set(b);
    for (var i = 0; i < a.length; i++) {
        if (set.has(v - a[i])) {
            return true;
        }
    }
    return false;
}
var result = sumOfTwo([1, 2, 3], [10, 20, 30, 40], 42); // false
console.log(result);
