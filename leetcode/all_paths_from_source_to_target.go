package main

import "fmt"

func allPathsSourceTarget(graph [][]int) [][]int {
	res := make([][][]int, len(graph))
	for i := 0; i < len(graph); i++ {
		res[i] = make([][]int, 0)
	}
	for i := len(graph) - 1; i >= 0; i-- {
		if i == len(graph)-1 {
			res[i] = append(res[i], []int{i})
		} else {
			arr := graph[i]

			for _, val := range arr {
				if len(res[val]) != 0 {
					for _, inVal := range res[val] {
						a := append(make([]int, 0), i)
						res[i] = append(res[i], append(a, inVal...))
					}
				}
			}
		}

	}
	return res[0]
}
func main() {
	graph := [][]int{{1, 2, 4}, {2, 3, 4}, {3, 5, 6}, {4, 5, 6}, {}, {7}, {7}, {}}
	res := allPathsSourceTarget(graph)
	fmt.Println(res)
}
