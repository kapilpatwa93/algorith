// https://leetcode.com/problems/binary-number-with-alternating-bits/
// 693. Binary Number with Alternating Bits
package main

import (
	"fmt"
	"math"
	"math/bits"
)

func hasAlternatingBits(n int) bool {
	num := uint(n)
	num2 := bits.RotateLeft(num,1)
	if num % 2  == 0 {
		num2 = num2 + 1
	}
	log := math.Log2(float64((num ^ num2)+1))
	return log == float64(int(log))
}
func main() {
	n := 10
	res := hasAlternatingBits(n)
	fmt.Println(res)
}
