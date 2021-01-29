package main

import (
	"fmt"
)

func canFormArray1(arr []int, pieces [][]int) bool {
	countMap := make(map[string]int)
	for _, piece := range pieces {
		countMap[getStringFromIntArr(piece)] = 1
	}
	//matched := false
	str := ""
	for _, num := range arr {
			str = fmt.Sprintf("%s%d",str,num)
			if countMap[str] == 1 {
				str = ""

			}
	}
	return str == ""
}
func canFormArray(arr []int, pieces [][]int) bool {
	prevI := 0
	for i := 0; i < len(arr); {
		for _, piece := range pieces {
			if i < len(arr) && arr[i] == piece[0] {
				for _, p := range piece {
					if i < len(arr) && p == arr[i]  {
						i++
					} else {
						return false
					}
				}
			}
		}
		if i == prevI {
			return false
		}
		prevI = i
	}
	return true

}
func getStringFromIntArr(arr []int) string  {
	s := ""
	for _, i := range arr {
		s = fmt.Sprintf("%s%d",s,i)
	}
	return s
}
func main() {
	arr := []int{92,4,33,2,6}
	pieces := [][]int {
		{4,33},
		{2,6},
		{92},
	}
	res := canFormArray(arr,pieces)
	fmt.Println(res)
}
