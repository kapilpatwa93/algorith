// https://leetcode.com/problems/find-the-duplicate-number/
// 287. Find the Duplicate Number
package main

import (
	"fmt"
	"math"
)

func findDuplicate(nums []int) int {
	for i := 0; i < len(nums); i++ {
		n := int(math.Abs(float64(nums[i])))
		nums[n] *= -1
		if nums[n] > 0 {
			return n
		}

	}
	return -1
}

func main() {
	nums := []int{3, 1, 3, 4, 2}
	res := findDuplicate(nums)
	fmt.Println(res)
}
