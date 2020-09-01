// https://leetcode.com/problems/maximal-square/
// 221. Maximal Square
package main

import (
	"fmt"
	"math"
)

func maximalSquare(matrix [][]byte) int  {
	max := 0
	if len(matrix) == 0 {
		return 0
	}
	rows := len(matrix)
	cols := len(matrix[0])
	memo := make([][]int,rows)
	for i := range memo {
		memo[i] = make([]int, cols)
	}
	for i :=0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			res :=recurse(matrix,i,j, memo)
			if  res > max {
				max = res
			}
		}
	}
	return max * max

}
func recurse(matrix [][]byte, i, j int, memo [][]int) int {
	if i >= len(matrix) || j >= len(matrix[0]) {
		return 0
	}

	if  memo[i][j] != 0{
		return memo[i][j]
	}
	if matrix[i][j] == '0' {
		return 0
	}
	right := recurse(matrix,i+1,j,memo)
	bottom := recurse(matrix,i,j+1,memo)
	diagonal := recurse(matrix,i+1,j+1,memo)
	memo[i][j] = 1 + int(math.Min(float64(right),math.Min(float64(bottom), float64(diagonal))))
	return memo[i][j]
}

func main() {
	matrix := [][]byte{
		{'1', '1', '1', '1', '1'},
		{'1', '1', '1', '1', '0'},
		{'0', '1', '1', '1', '1'},
		{'0', '1', '0', '1', '1'}}
	res := maximalSquare(matrix)
	fmt.Println(res)
}
