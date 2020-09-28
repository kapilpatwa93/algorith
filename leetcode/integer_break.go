// https://leetcode.com/problems/integer-break/
// 343. Integer Break
package main

import "fmt"

func integerBreak(n int) int {
	if n <=3 {
		return n-1
	}
	res := 1
	for;n > 0; {
		if n == 4 {
			n = n-4
			res = res * 4
		} else if n > 4  || n == 3 {
			n-=3
			res = res * 3
		} else if n == 2 {
			n-=2
			res = res * 2
		}
	}
	return res
}
func main() {
	n := 10
	res := integerBreak(n)
	fmt.Println(res)
}
