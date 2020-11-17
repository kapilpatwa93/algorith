package main

import "fmt"

func longestPalindrome(s string) int {
	charMap := make(map[byte]int)
	for _, b := range []byte(s) {
		charMap[b]++
	}
	oddPresent := false
	total := 0
	for _, count := range charMap {
		if count % 2  == 0 {
			total += count
		} else {
			oddPresent = true
			total += count - 1
		}
	}
	if oddPresent {
		total++
	}
	return total
}

func main() {
	s := "bb"
	res := longestPalindrome(s)
	fmt.Println(res)
}
