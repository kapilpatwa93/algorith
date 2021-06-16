
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var findDiagonalOrder = function (matrix) {
    let arr = [];
    let iOffset = -1;
    let jOffset = 1;
    let x = 0;
    let y = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j <= i; j++) {
            // console.log(stones[x][y])
            arr.push(matrix[x][y])
            x += iOffset;
            y += jOffset
        }
        if (iOffset == 1) {
            y -= jOffset
        } else {
            x -= iOffset
        }

        iOffset *= -1;
        jOffset *= -1;

    }
    x += iOffset
    y += jOffset
    for (let i = matrix.length - 1; i > 0; i--) {

        for (let j = i; j > 0; j--) {
            // let num = stones[x][y];
            // console.log(stones[x][y])
            arr.push(matrix[x][y])
            x += iOffset;
            y += jOffset
        }
        iOffset *= -1;
        jOffset *= -1;
        if (iOffset == -1) {
            y += jOffset
            y += jOffset
            x += iOffset


        } else {
            y += jOffset
            x += iOffset
            x += iOffset

        }


    }
    return arr;
};

function main() {
    // let stones = [
    //     [1,2,3],
    //     [4,5,6],
    //     [7,8,9],
    // ];
    let stoness = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    let stones = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    let res = findDiagonalOrder(stones);
    console.log(res);
}

main()
