// https://leetcode.com/problems/add-strings/submissions/
// 415. Add Strings
package main

import (
	"fmt"
	"strconv"
)

func addStrings(num1 string, num2 string) string {
	maxLen := len(num1)
	minLen := len(num2)
	bigNum := num1
	smallNum := num2
	if maxLen < len(num2) {
		maxLen = len(num2)
		bigNum = num2
		smallNum = num1
		minLen = len(num1)
	}
	carry := 0
	sum := ""
	for i := 0; i < maxLen; i++ {
		d, _ := strconv.Atoi(string(bigNum[maxLen-i-1]))
		d += carry
		if i < minLen {
			d2, _ := strconv.Atoi(string(smallNum[minLen-i-1]))
			d += d2
		}
		sum = strconv.Itoa(d%10) + sum
		carry = d / 10
	}
	if carry != 0 {
		sum = strconv.Itoa(carry%10) + sum
	}
	return sum
}
func main() {
	num1 := "9999"
	num2 := "9999"
	res := addStrings(num1, num2)
	fmt.Println(res)
}
