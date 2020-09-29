// https://leetcode.com/problems/flip-string-to-monotone-increasing/
// 926. Flip String to Monotone Increasing
package main

import (
	"fmt"
	"math"
	"strconv"
)

func minFlipsMonoIncr(S string) int {
	prefixSum := make([]int, len(S)+1)
	for i, val := range []byte(S) {
		n, _ := strconv.Atoi(string(val))
		prefixSum[i+1] = prefixSum[i] + n
	}
	ans := math.MaxInt32
	for j := 0; j <= len(S); j++ {
		s := prefixSum[j] + len(S) - j - (prefixSum[len(S)] - prefixSum[j])
		if ans > s {
			ans = s
		}
	}
	return ans
}

func main() {
	S := "010110"
	res := minFlipsMonoIncr(S)
	fmt.Println(res)
}
