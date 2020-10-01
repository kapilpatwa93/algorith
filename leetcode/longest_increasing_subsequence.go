// https://leetcode.com/problems/longest-increasing-subsequence/solution/
// 300. Longest Increasing Subsequence
package main

import "fmt"

func lengthOfLIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	tab := make([]int, len(nums))
	tab[0] = 1
	res := 1
	for i := 1; i < len(nums); i++ {
		max := 0
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				if max < tab[j] {
					max = tab[j]
				}
			}
		}
		tab[i] = max + 1
		if res < tab[i] {
			res = tab[i]
		}
	}
	return res
}

func main() {
	nums := []int{1, 3, 5, 6, 7, 4, 6, 7, 8, 1, 4, 5}
	res := lengthOfLIS(nums)
	fmt.Println(res)
}
