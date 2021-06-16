package main

import (
	"fmt"
	"math"
)

func maximalSquare(matrix [][]int) int {
	max := 0
	rows := len(matrix)
	cols := len(matrix[0])
	tab := make([][]int, rows)
	for i := range tab {
		tab[i] = make([]int, cols)
	}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {

			if i < 1 || j < 1 {
				tab[i][j] = 0
			}
		}
	}
	return max * max

}
func getTab()
func min(a, b, c int) int {
	if a < b && a < c {
		return a
	} else if b < a && b < c {
		return b
	}
	return c
}
func recurse(matrix [][]byte, i, j int, memo [][]int) int {
	if i >= len(matrix) || j >= len(matrix[0]) {
		return 0
	}
	if memo[i][j] != 0 {
		return memo[i][j]
	}
	if matrix[i][j] == 0 {
		return 0
	}
	right := recurse(matrix, i+1, j, memo)
	bottom := recurse(matrix, i, j+1, memo)
	diagonal := recurse(matrix, i+1, j+1, memo)
	memo[i][j] = 1 + int(math.Min(float64(right), math.Min(float64(bottom), float64(diagonal))))
	return memo[i][j]
}
func main() {
	matrix := [][]int{
		{1, 1, 1, 1, 1},
		{1, 1, 1, 1, 0},
		{0, 1, 1, 1, 1},
		{0, 1, 0, 1, 1}}
	res := maximalSquare(matrix)
	fmt.Println(res)
}
