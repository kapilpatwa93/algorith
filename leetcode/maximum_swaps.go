// https://leetcode.com/problems/maximum-swap/solution/
// 670. Maximum Swap
package main

import (
	"fmt"
	"sort"
	"strconv"
)

type Num struct {
	num int
	pos int
}

func maximumSwap(num int) int {
	var numPos []Num
	str := strconv.Itoa(num)
	pos := 0
	var numArr []int
	for _, i2 := range str {
		num, _ := strconv.Atoi(string(i2))
		numArr = append(numArr, num)
		numPos = append(numPos, Num{
			num: num,
			pos: pos,
		})
		pos++
	}
	sort.Slice(numPos, func(i, j int) bool {
		return numPos[i].num > numPos[j].num || (numPos[i].num == numPos[j].num && numPos[i].pos < numPos[j].pos)
	})
	for i, v := range numArr {
		if v < numPos[i].num {
			i1 := i
			for ; i < len(numArr)-1; {
				if numPos[i].num == numPos[i+1].num {
					i++
				} else {
					break
				}
			}
			numArr[i1], numArr[numPos[i].pos] = numPos[i].num, numArr[i1]
			break
		}
	}
	v := 0
	for _, val := range numArr {
		v = v*10 + val
	}
	return v
}

func main() {
	//num := 6215
	num := 19992
	res := maximumSwap(num)
	fmt.Println(res)
	fmt.Println()
}
