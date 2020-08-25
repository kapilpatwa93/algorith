// https://leetcode.com/problems/numbers-with-same-consecutive-differences/submissions/
// 967. Numbers With Same Consecutive Differences
package main

import (
	"fmt"
	"math"
)

func numsSameConsecDiff(N int, K int) []int {
	if N == 1 {
		res := make([]int, 10)
		for i := 0; i < 10; i++ {
			res[i] = i
		}
		return res
	}
	numMap := make(map[int][]int)
	for i := 0; i <= 9; i++ {
		var arr []int
		for j := 0; j <= 9; j++ {
			if int(math.Abs(float64(i-j))) == K {
				arr = append(arr, j)
			}
			if len(arr) != 0 {
				numMap[i] = arr
			}

		}
	}
	var res []int
	for key := range numMap {
		if key != 0 {
			res = append(res, key)
		}

	}
	for i := 1; i < N; i++ {
		var newRes []int
		for _, val := range res {
			lastNum := val % 10
			nArray := numMap[lastNum]
			for _, nVal := range nArray {
				newRes = append(newRes, val*10+nVal)
			}
		}
		res = newRes
	}
	return res
}
func main() {
	n := 3
	k := 7
	res := numsSameConsecDiff(n, k)
	fmt.Println(res)
}
