// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
// 1013. Partition Array Into Three Parts With Equal Sum
package main

import "fmt"

func canThreePartsEqualSum(A []int) bool {
	sum := 0
	for _, val := range A {
		sum += val
	}
	fmt.Println(sum)
	if sum%3 != 0 {
		return false
	}
	part := sum / 3
	partSum := 0
	res := false
	count := 0
	for i := 0; i < len(A); i++ {
		partSum += A[i]
		if part == partSum {
			fmt.Println(partSum, i)
			count++
			partSum = 0
		}
		if count == 3 {
			res = true
			break
		}

	}
	return res
}

func main() {
	A := []int{0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1}
	res := canThreePartsEqualSum(A)
	fmt.Println(res)
}
