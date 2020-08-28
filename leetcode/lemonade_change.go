// https://leetcode.com/problems/lemonade-change/
// 860. Lemonade Change
package main

import "fmt"

func lemonadeChange(bills []int) bool {
	ans := true
	collection := make(map[int]int)
	for _, amount := range bills {
		switch amount {
		case 5:
			collection[5] += 1
		case 10:
			if collection[5] == 0 {
				ans = false
				break
			}
			collection[10] += 1
			collection[5] -= 1
		case 20:
			if collection[10] == 0 {
				if collection[5] < 3 {
					ans = false
					break

				}
				collection[5] -= 3
			} else {
				if collection[5] < 1 {
					ans = false
					break

				}
				collection[5] -= 1
				collection[10] -= 1
			}
			collection[20] += 1
		}
	}
	return ans
}
func main() {
	bills := []int{5, 5, 5, 10, 20}
	res := lemonadeChange(bills)
	fmt.Println(res)
}
