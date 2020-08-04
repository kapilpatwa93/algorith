// https://leetcode.com/problems/gray-code/
// 89. Gray Code
/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    let binaryArr = [];
    let map = {};
    let responseArr = [];
    for (let i = 0; i < Math.pow(2, n); i++) {
        binaryArr.push(i.toString(2).padStart(n, 0));
    }
    responseArr.push(binaryArr[0]);
    map[binaryArr[0]] = 1
    for (let i = 0; i < Math.pow(2, n) - 1; i++) {
        let s = responseArr[responseArr.length - 1];
        let splitArr = s.split('');
        for (let i = splitArr.length - 1; i >= 0; i--) {
            let splitArrCopy = splitArr.slice();
            splitArrCopy[i] = splitArrCopy[i] === 0 ? 1: 0
            let newString = splitArrCopy.join('');
            if (!map[newString]) {
                responseArr.push(newString);
                map[newString] = 1;
                break;
            }
        }
    }
    return responseArr.map((s) => parseInt(s,2));
};
function main() {
    let n = 3;
    let res = grayCode(n);
    console.log(res);
}
main()
