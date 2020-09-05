// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
// 1209. Remove All Adjacent Duplicates in String II
package main

import (
	"fmt"
	"strings"
)

func removeDuplicates(s string, k int) string {
	stack := make([]string, len(s))
	sameLengthArr := make([]int, len(s))
	prev := ""
	top := 0
	for _, c := range s {
		stack[top] = string(c)
		if prev == stack[top] {
			sameLengthArr[top] = sameLengthArr[top-1] + 1
			if sameLengthArr[top] == k {
				top = top - k
			}
		} else {
			sameLengthArr[top] = 1
		}
		if top == -1 {
			prev = ""
		} else {
			prev = stack[top]
		}
		top++
	}
	return strings.Join(stack[0:top], "")
}

func main() {
	s := "kakppkaapa"
	k := 2
	res1 := removeDuplicates(s, k)
	fmt.Println(res1)
}
