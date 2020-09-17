// https://leetcode.com/problems/find-lucky-integer-in-an-array/
// 1394. Find Lucky Integer in an Array
package main

import "fmt"

func findLucky(arr []int) int {
	freqMap := make(map[int]int)
	for _,num := range arr {
		freqMap[num] += 1
	}

	lucky := -1
	for key,freq := range freqMap {
		if key == freq && lucky < freq {
			lucky = freq
		}
	}
	return lucky
}

func main() {
	arr := []int{2,2,3,4}
	res := findLucky(arr)
	fmt.Println(res)
}
