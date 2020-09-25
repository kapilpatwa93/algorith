// https://leetcode.com/problems/unique-paths-ii/
// 63. Unique Paths II

package main

import "fmt"

// Solving using Bottom Up Approach
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	xMax := len(obstacleGrid)
	yMax := len(obstacleGrid[0])
	tab := make([][]int, xMax, yMax)
	for i := 0; i < len(obstacleGrid); i++ {
		tab[i] = make([]int, yMax)
	}
	getTab := func(i, j int) int {
		if i >= xMax || j >= yMax {
			return 0
		}
		return tab[i][j]
	}

	tab[xMax-1][yMax-1] = 1
	if obstacleGrid[xMax-1][yMax-1] == 1 {
		tab[xMax-1][yMax-1] = 0
	}
	for i := xMax - 1; i >= 0; i-- {
		for j := yMax - 1; j >= 0; j-- {
			if obstacleGrid[i][j] == 0 {
				tab[i][j] = getTab(i+1, j) + getTab(i, j+1) + tab[i][j]
			}

		}
	}
	return tab[0][0]
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
