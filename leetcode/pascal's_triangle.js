// https://leetcode.com/problems/pascals-triangle/
// 118. Pascal's Triangle
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
    if (numRows <= 0) {
        return []
    }
    let res = [[1]];
    function getNumber(currRow, currCol) {
        if (res[currRow] && res[currRow][currCol]) {
            return res[currRow][currCol]
        }
        return 0;
    }
    for (let i = 1; i < numRows; i++) {
        let arr = [];
        for (let j = 0; j <= i; j++) {
            arr.push(getNumber(i - 1, j - 1) + getNumber(i - 1, j))

        }
        res.push(arr);
    }
    return res;
};

function main() {
    let rows = 5;
    let res = generate(rows);
    console.log(res);
}

main()
