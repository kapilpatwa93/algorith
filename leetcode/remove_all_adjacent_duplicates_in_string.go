// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
// 1047. Remove All Adjacent Duplicates In String
package main

import (
	"fmt"
	"strings"
)

func removeDuplicates(s string) string {
	stack := make([]string, len(s))
	prev := ""
	sameLength := 1
	top := 0
	for _, c := range s {
		stack[top] = string(c)
		if prev == stack[top] {
			sameLength += 1
			if sameLength == 2 {
				top = top - 2
				sameLength = 1
			}
		} else {
			sameLength = 1
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
	s := "abbaca"
	res := removeDuplicates(s)
	fmt.Println(res)
}
