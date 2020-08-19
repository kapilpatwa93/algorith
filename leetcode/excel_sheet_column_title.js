// https://leetcode.com/problems/excel-sheet-column-title/
// 168. Excel Sheet Column Title
/**
 * @param {number} n
 * @return {string}
 */
var convertToTitle = function (n) {
    let a = "A".charCodeAt(0);
    let title = "";
    n = n - 1;
    while (n >= 0) {
        title = String.fromCharCode((n % 26) + a) + title;
        n = Math.floor(n / 26) - 1
    }
    return title;
};

function main() {
    let n = 26;
    let res = convertToTitle(n);
    console.log(res);
}

main();
