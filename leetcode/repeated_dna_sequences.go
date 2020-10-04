// https://leetcode.com/problems/repeated-dna-sequences/
// 187. Repeated DNA Sequences

package main

import "fmt"

func findRepeatedDnaSequences(s string) []string {
	m := make(map[string]int)
	charArray := []rune(s)
	for i := 0; i < len(s)-9; i++ {
		s1 := string(charArray[i:i+10])
		m[s1] += 1
	}

	res := make([]string, 0)
	for k, val := range m {
		if val >= 2 {
			res = append(res, k)
		}
	}
	return res
}
func main() {
	s := "AAAAAAAAAAA"
	res := findRepeatedDnaSequences(s)
	fmt.Println(res)
}
