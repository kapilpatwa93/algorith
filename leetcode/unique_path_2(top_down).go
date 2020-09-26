// https://leetcode.com/problems/unique-paths-ii/
// 63. Unique Paths II

package main

import "fmt"

// Solving using Top Down Approach
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	memo := make([][]int, len(obstacleGrid))
	for i := 0; i < len(obstacleGrid); i++ {
		memo[i] = make([]int, len(obstacleGrid[0]))
	}
	return getPathCount(&obstacleGrid, &memo, 0, 0)

}
func getPathCount(obstacle, memo *[][]int, i, j int) int {
	if i >= len(*obstacle) || j >= len((*obstacle)[0]) || (*obstacle)[i][j] == 1 {
		return 0
	}
	if i == len(*obstacle)-1 && j == len((*obstacle)[0])-1 {
		return 1
	}
	if (*memo)[i][j] != 0 {
		return (*memo)[i][j]
	}
	right := getPathCount(obstacle, memo, i, j+1)
	bottom := getPathCount(obstacle, memo, i+1, j)
	if bottom != 0 {
		(*memo)[i+1][j] = getPathCount(obstacle, memo, i+1, j)
	}
	if right != 0 {
		(*memo)[i][j+1] = getPathCount(obstacle, memo, i, j+1)
	}
	return right + bottom
}

func main() {
	obstacleGrid := [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	res := uniquePathsWithObstacles(obstacleGrid)
	fmt.Println(res)
}
