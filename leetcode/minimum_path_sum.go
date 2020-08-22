// https://leetcode.com/problems/minimum-path-sum/
// 64. Minimum Path Sum
package main

import (
	"fmt"
)

var minMap = make(map[string]int)

func minPathSum(grid [][]int) int {
	return recurse(grid, 0, 0)
}
func recurse(grid [][]int, row, col int) int {
	if row == len(grid)-1 && col == len(grid[0])-1 {
		return grid[row][col]
	}
	key := fmt.Sprintf("%s%s", row, col)
	if res, present := minMap[key]; present {
		return res
	}
	if row >= len(grid) || col >= len(grid[0]) {
		return 9999999
	}
	cur := grid[row][col]
	right := recurse(grid, row, col+1) + cur
	down := recurse(grid, row+1, col) + cur
	min := right
	if down < min {
		min = down
	}
	minMap[key] = min
	return min

}

func main() {
	grid := [][]int{
		{1, 10, 1},
		{1, 5, 1},
		{4, 2, 1},
	}
	res := minPathSum(grid)
	fmt.Println(res)
}
