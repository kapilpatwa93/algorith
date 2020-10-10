// https://leetcode.com/problems/same-tree/submissions/
// 100. Same Tree
package main

import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
	return recurse(p,q)
}
func recurse(p,q *TreeNode) bool  {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	if p.Val != q.Val {
		return false
	}
	return recurse(p.Left,q.Left) && recurse(p.Right,q.Right)
}
func main() {
	input1 := []int{1, 2, 2, 3, 3, 4, 3}
	input2 := []int{1, 2, 2, 3, 4, 4, 3}
	p := makeTree(input1)
	q := makeTree(input2)
	res := isSameTree(p,q)
	fmt.Println(res)
}

func makeTree(input []int) *TreeNode {
	return getTree(0, input)
}
func getTree(subRootIndex int, input []int) *TreeNode {
	if subRootIndex >= len(input) || input[subRootIndex] == -1 {
		return nil
	}
	return MakeTreeNode(input[subRootIndex], getTree((subRootIndex*2)+1, input), getTree((subRootIndex+1)*2, input))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func MakeTreeNode(val int, left, right *TreeNode) *TreeNode {
	return &TreeNode{
		Val:   val,
		Left:  left,
		Right: right,
	}
}
