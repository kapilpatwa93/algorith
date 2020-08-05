// https://leetcode.com/problems/valid-sudoku/
// 36. Valid Sudoku
/**
 * @param {string[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    let rowMaps = [];
    let colMaps = [];
    let boxMaps = [];
    for (let i = 0; i < 3; i++) {
        boxMaps.push([]);
        for (let j = 0; j < 3; j++) {
            colMaps.push({});
            rowMaps.push({});
            boxMaps[i].push({})
        }
    }
    let res = true;
    outer : for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            let num = board[i][j];
            if (num !== ".") {
                if (rowMaps[i][num]) {
                    res = false;
                    break outer;
                } else {
                    rowMaps[i][num] = 1;
                }
                if (colMaps[j][num]) {
                    res = false;
                    break outer;
                } else {
                    colMaps[j][num] = 1;
                }
                if (boxMaps[parseInt(i/3)][parseInt(j/3)][num]) {
                    res = false;
                    break outer;
                } else {
                    boxMaps[parseInt(i/3)][parseInt(j/3)][num] = 1;
                }
            }
        }
    }
    return res;
};
function main() {
    let board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ];
    let res = isValidSudoku(board);
    console.log(res);
}
main()
