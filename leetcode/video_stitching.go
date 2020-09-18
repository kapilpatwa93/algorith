// https://leetcode.com/problems/video-stitching/
// 1024. Video Stitching
package main

import (
	"fmt"
	"sort"
)

func videoStitching(clips [][]int, T int) int {
	sort.Slice(clips, func(i, j int) bool {
		return clips[i][0] < clips[j][0] || clips[i][0] == clips[j][0] && clips[i][1] < clips[j][1]
	})
	pointer := -1
	tab := make([]int, len(clips))
	for i := 0; i < len(clips); i++ {
		if clips[i][0] != 0 {
			break
		}
		tab[i] = 1
		pointer++
	}
	if pointer == -1 {
		return -1
	}
	c := 0
	vCount := 2
	for ; c < len(clips); {
		for j := pointer + 1; j < len(clips); j++ {
			c++
			if clips[j][0] <= clips[pointer][1] {
				tab[j] = vCount

			} else {
				pointer = j - 1
				vCount++
				break
			}
		}
	}
	for i := 0; i < len(clips); i++ {
		if clips[i][1] >= T {
			if tab[i] <= 0 {
				return -1
			} else {
				return tab[i]
			}
		}
	}
	return -1
}
func main() {
	clips := [][]int{{0, 2}, {4, 6}, {8, 10}, {1, 9}, {1, 5}, {5, 9}}
	t := 10
	res := videoStitching(clips, t)
	fmt.Println(res)

}
