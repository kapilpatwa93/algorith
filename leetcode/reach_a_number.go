// https://leetcode.com/problems/reach-a-number/
// 754. Reach a Number
package main

import (
	"fmt"
)

func reachNumber(target int) int {
	if target < 0 {
		target *= -1
	}
	n := 0
	counter := 1
	for {
		if n == target {
			return counter - 1
		}
		if n > target {
			diff := n - target
			if diff%2 == 0 {
				return counter - 1
			} else {
				if (diff+counter)%2 == 0 {
					return counter
				} else {
					return counter + 1
				}
			}
		}
		n += counter
		counter++
	}

}

func main() {
	target := 5
	res := reachNumber(target)
	fmt.Println(res)
}
