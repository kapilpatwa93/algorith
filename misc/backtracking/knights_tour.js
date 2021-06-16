
const findKnightsTour = function (x, y, size) {
    const isValidPosition = (x, y) => x >= 0 && x < size && y >= 0 && y < size
    const isVisited = (x, y) => board[x][y] !== -1
    const possibleMoves = [
        [1, 2],
        [2, 1],
        [-1, 2],
        [-2, 1],
        [-2, -1],
        [-1, -2],
        [1, -2],
        [2, -1],
    ];
    let totalSize = size * size

    function next(board, x, y, move) {
        if (move === totalSize) {
            return board
        }
        for (let i = 0; i < 8; i++) {
            let newX = x + possibleMoves[i][0];
            let newY = y + possibleMoves[i][1];
            if (isValidPosition(newX, newY) && !isVisited(newX, newY)) {
                board[newX][newY] = move;
                let solved = next(board, x + possibleMoves[i][0], y + possibleMoves[i][1], move + 1)
                if (solved) {
                    return solved;
                } else {
                    board[newX][newY] = -1;
                }
            }
        }
        return null;
    }

    let board = [];
    for (let i = 0; i < size; i++) {
        board.push(new Array(size).fill(-1))
    }
    if (!isValidPosition(x,y)) {
        return  null
    }
    board[x][y] = 0;
    return next(board, x, y, 1);
}


function main() {
    let solved = findKnightsTour(7, 7, 8);
    console.log(solved);

}

main()
