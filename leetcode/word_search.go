// https://leetcode.com/problems/word-search/
// 79. Word Search
package main

import "fmt"

func exist(board [][]byte, word string) bool {
	wordChar := []byte(word)
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if check(&board, wordChar, 0, i, j) {
				return true
			}
		}
	}
	return false
}
func check(board *[][]byte, word []byte, curr, i, j int) bool {
	if curr >= len(word) {
		return true
	}
	if i >= len((*board)) || j >= len((*board)[0]) || i < 0 || j < 0 {
		return false
	}
	if (*board)[i][j] != word[curr] {
		return false
	}
	c := (*board)[i][j]
	(*board)[i][j] = '-'
	right := check(board, word, curr+1, i, j+1)
	left := check(board, word, curr+1, i, j-1)
	bottom := check(board, word, curr+1, i+1, j)
	top := check(board, word, curr+1, i-1, j)
	isTrue := right || left || top || bottom
	if !isTrue {
		(*board)[i][j] = c
	}
	return isTrue
}
func main() {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	word := "ABCCED"
	res := exist(board, word)
	fmt.Println(res)
}
