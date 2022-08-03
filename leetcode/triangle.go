package main

import (
	"fmt"
)

func mini(i, j int) int {
	if i < j {
		return i
	}
	return j
}
func minimumTotal(triangle [][]int) int {
	newrow := []int{}
	getPrevMinimum := func(row, col int) int {
		if row == 0 || row >= len(triangle) {
			return 0
		}
		if col == len(triangle[row])-1 {
			return newrow[col-1]
		}
		if col == 0 {
			return newrow[0]
		}
		return mini(newrow[col-1], newrow[col])
	}
	m := 0
	for i, row := range triangle {
		n1 := []int{}
		m = 100000
		for j, val := range row {
			v := getPrevMinimum(i, j) + val
			n1 = append(n1, v)
			m = mini(m, v)
		}
		newrow = n1
	}
	//fmt.Println(m)
	return m
}

func main() {
	triangle := [][]int{
		{2},
		{3, 4},
		{6, 5, 7},
		{4, 1, 8, 3},
	}
	res := minimumTotal(triangle)
	fmt.Println(res)
}

//    {2},
//  {3, 4},
// {6, 5, 7},
//{4, 1, 8, 3},
