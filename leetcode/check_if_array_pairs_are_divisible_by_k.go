// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/submissions/
// 1497. Check If Array Pairs Are Divisible by k
package main

import "fmt"

func canArrange(arr []int, k int) bool {
	m := make(map[int]int)
	for i := 0; i < len(arr); i++ {
		arr[i] = (arr[i]%k + k) % k
		m[arr[i]] += 1
	}
	for i := 0; i < len(arr); i++ {
		if m[arr[i]] != 0 && m[(k-arr[i])%k] != 0 {
			m[arr[i]] -= 1
			m[(k-arr[i])%k] -= 1
		}
	}
	for _, v := range m {
		if v >= 1 || v < 0 {
			return false
		}
	}
	return true
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 10, 6, 7, 8, 9}
	k := 10
	res := canArrange(arr, k)
	fmt.Println(res)
}
