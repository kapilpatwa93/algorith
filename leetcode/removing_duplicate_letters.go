// https://leetcode.com/problems/remove-duplicate-letters/
// 316. Remove Duplicate Letters
package main

import (
	"fmt"
	"strings"
)

func removeDuplicateLetters(s string) string {
	occMap := make(map[string]int)
	useMap := make(map[string]int)
	for i, val := range []byte(s) {
		occMap[string(val)] = i
		useMap[string(val)] = 0
	}
	stackPtr := -1
	stack := make([]string, len(occMap))
	for i, c := range []byte(s) {
		s := string(c)
		if stackPtr >= 0 && stack[stackPtr] > s && useMap[s] == 0 && occMap[stack[stackPtr]] > i {
			for {
				if i >= 0 && stackPtr >= 0 && stack[stackPtr] > s && useMap[s] == 0 && occMap[stack[stackPtr]] > i {
					useMap[stack[stackPtr]] = 0
					stackPtr--
				} else {
					break
				}
			}
			stackPtr++
			stack[stackPtr] = s
			useMap[s] = 1
		} else if useMap[s] == 0 {
			stackPtr++
			stack[stackPtr] = s
			useMap[s] = 1
		}
	}
	return strings.Join(stack, "")
}

func main() {
	res := removeDuplicateLetters("bcabc")
	fmt.Println(res)
}
