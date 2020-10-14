// https://leetcode.com/problems/set-matrix-zeroes/
// 73. Set Matrix Zeroes
var setZeroes = function (matrix) {
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] == 0 && j != 0) {
                if (matrix[i][0] != 0) {
                    matrix[i][0] = "r"
                }

            }
        }
    }
    for (let i = 0; i < matrix.length; i++) {
        if (matrix[i][0] == "r" || matrix[i][0] == 0) {
            for (let j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] != 0) {
                    matrix[i][j] = null
                }
            }
        }
    }
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] == 0 && i != 0) {
                if (matrix[0][j] != 0) {
                    matrix[0][j] = "d"
                }
            }
        }
    }
    for (let j = 0; j < matrix[0].length; j++) {
        if (matrix[0][j] == "d" || matrix[0][j] == 0) {
            for (let i = 0; i < matrix.length; i++) {
                if (matrix[i][j] != 0) {
                    matrix[i][j] = null
                }
            }
        }

    }
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] == null) {
                matrix[i][j] = 0
            }
        }
    }

};
function main() {
    let matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(matrix)
    console.log(matrix);
}
main()

