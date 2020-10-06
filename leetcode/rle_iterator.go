// https://leetcode.com/problems/rle-iterator/
// 900. RLE Iterator
package main

import "fmt"

type RLEIterator struct {
	arr []int
	cur int
}

func Constructor(A []int) RLEIterator {
	return RLEIterator{arr: A, cur: 0}
}

func (this *RLEIterator) Next(n int) int {
	for ; n >= 0 && (*this).cur < len((*this).arr)-1; {
		if n > (*this).arr[(*this).cur] {
			n -= (*this).arr[(*this).cur]
			(*this).cur += 2
		} else if n <= (*this).arr[(*this).cur] {
			(*this).arr[(*this).cur] -= n
			break
		}

	}
	if (*this).cur >= len((*this).arr)-1 {
		return -1
	}
	return (*this).arr[(*this).cur+1]
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * obj := Constructor(A);
 * param_1 := obj.Next(n);
 */
func main() {
	arr := [][]int{{3, 8, 0, 9, 2, 5}, {2}, {1}, {1}, {2}}
	rle := Constructor(arr[0])
	for i := 1; i < len(arr); i++ {
		fmt.Println(rle.Next(arr[i][0]))
	}

}
