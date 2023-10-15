function sumOfTwo(a: number[], b: number[], v: number): boolean {
    const set = new Set(b);
    for (let i = 0; i < a.length; i++) {
      if (set.has(v - a[i])) {
        return true;
      }
    }
    return false;
  }

const result = sumOfTwo([1, 2, 3], [10, 20, 30, 40], 42); // false
console.log(result);