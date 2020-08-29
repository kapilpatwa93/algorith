// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
// 1072. Flip Columns For Maximum Number of Equal Rows
package main

import "fmt"

func maxEqualRowsAfterFlips(matrix [][]int) int {
	countMap := make(map[string]int)
	for i := 0; i < len(matrix); i++ {
		zeros := ""
		ones := ""
		for j := 0; j < len(matrix[i]) ; j++ {
			if matrix[i][j] == 0 {
				zeros += string(j)
			} else {
				ones += string(j)
			}
		}
		countMap[zeros] += 1
		countMap[ones] += 1
	}
	res := 0
	for _, val := range countMap {
		if val > res {
			res = val
		}
	}
	return res
}
func main() {
	matrix := [][]int{{1,0,0,1},{1,0,1,0}, {0,1,1,0}, {1,0,0,1}}
	res := maxEqualRowsAfterFlips(matrix)
	fmt.Println(res)

}
