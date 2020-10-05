package main

import (
	"fmt"
	"sort"
)

func insert(intervals [][]int, newInterval []int) [][]int {
	intervals = append(intervals, newInterval)
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})
	res := make([][]int, 0)
	for i := 0; i < len(intervals); i++ {
		curr := intervals[i]
		max := curr[1]
		j := i
		for ; j < len(intervals); {
			if max >= intervals[j][0] {
				if max < intervals[j][1] {
					max = intervals[j][1]
				}
				j++
			} else {
				break
			}

		}
		res = append(res, []int{curr[0], max})
		i = j - 1
	}
	return res
}

func main() {
	intervals := [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}
	newInterval := []int{4, 8}
	res := insert(intervals, newInterval)
	fmt.Println(res)

}
