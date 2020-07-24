// https://leetcode.com/problems/unique-paths/
// 62. Unique Paths
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
let map = {};
function recurse(m,n) {
    if (n == 1) {
        return 1
    }
    let count = 1;
    for (let i = 2; i <= m; i++) {
        let sum = 0;
        if (map[`${Math.max(i,n-1)}${Math.min(i,n-1)}`]) {
            sum = map[`${Math.max(i,n-1)}${Math.min(i,n-1)}`]
        } else {
            sum = recurse(i,n-1);
            map[`${Math.max(i,n-1)}${Math.min(i,n-1)}`] = sum;
        }
        count += sum
    }
    return count;
}
var uniquePaths = function(m, n) {
    return recurse(m,n);

};

function main() {
    let res = uniquePaths(10,10);
    console.log(res);
}

main()
