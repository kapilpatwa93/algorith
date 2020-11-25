package main

import "fmt"

func maxDepth(s string) int {
	count := 0
	max := 0
	brackets := []byte("()")
	for _, char := range []byte(s) {
		if char == brackets[0] {
			count++
		} else if char == brackets[1] {
			count--
		}
		if count > max {
			max = count
		}
	}
	return max
}

func main() {
	s := "(1+(2*3)+((8)/4))+1"
	res := maxDepth(s)
	fmt.Println(res)
}
