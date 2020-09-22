// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// 17. Letter Combinations of a Phone Number
package main

import (
	"fmt"
	"strconv"
)

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	numMap := [][]string{{"a", "b", "c"}, {"d", "e", "f"}, {"g", "h", "i"}, {"j", "k", "l"}, {"m", "n", "o"}, {"p", "q", "r", "s"}, {"t", "u", "v"}, {"w", "x", "y", "z"}}
	var arr [][]string
	for _, val := range []rune(digits) {
		num, _ := strconv.Atoi(string(val))
		arr = append(arr, numMap[num-2])
	}
	return getCombinations(arr)
}

func getCombinations(arr [][]string) []string {
	return recursion(arr, 0, "")
}

func recursion(arr [][]string, current int, str string) []string {
	if current >= len(arr) {
		return []string{str}
	}
	a := arr[current]
	var col []string
	for i := 0; i < len(a); i++ {
		col = append(col, recursion(arr, current+1, fmt.Sprintf("%s%s", str, a[i]))...)
	}
	return col
}

func main() {
	digits := "23"
	res := letterCombinations(digits)
	fmt.Println(res)
}
