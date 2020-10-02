// https://leetcode.com/problems/majority-element/
// 169. Majority Element
package main

import "fmt"

func majorityElement(nums []int) int {
	// Boyer-Moore Voting Algorithm
	count := 0
	candidate := -1
	for i := 0; i < len(nums); i++ {
		if count == 0 {
			candidate = nums[i]
		}
		if candidate == nums[i] {
			count +=1
		} else {
			count -=1
		}
	}
	return candidate
}
func main() {
	nums := []int{7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 5, 5, 5, 5, 5, 5}
	res := majorityElement(nums)
	fmt.Println(res)
}
