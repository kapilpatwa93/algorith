//48. Rotate Image
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
    let len = matrix.length;
    let i = 0;
    while(i < (len / 2)) {
        for (let j = i; j < len -1 - i ; j++)  {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[len - 1 - j][i];
            matrix[len - 1 - j][i] = matrix[len - 1 - i][len - 1 - j];
            matrix[len - 1 - i][len - 1 - j] = matrix[j][len - i - 1];
            matrix[j][len - i - 1] = temp
        }
       i++
    }
};

function main() {
    let arr = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25],
    ]
    rotate(arr);
    console.log(arr);
}
main();
