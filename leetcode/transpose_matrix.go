// https://leetcode.com/problems/transpose-matrix
// 867. Transpose Matrix
package main

import "fmt"

func transpose(A [][]int) [][]int {
	var newArr [][]int
	for i := 0; i < len(A[0]); i++ {
		newArr = append(newArr, []int{})
		for j := 0; j < len(A); j++ {
			newArr[i] = append(newArr[i], A[j][i])
		}
	}
	return newArr
}
func main() {
	A := [][]int{{1, 2, 3}, {4, 5, 6}}
	res := transpose(A)
	fmt.Println(res)
}
