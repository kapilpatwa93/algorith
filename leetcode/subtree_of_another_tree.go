// https://leetcode.com/problems/subtree-of-another-tree/
// 572. Subtree of Another Tree
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

func isSubtree(s *TreeNode, t *TreeNode) bool {
	return traverse(s, t)
}

func traverse(s *TreeNode, t *TreeNode) bool {
	if s == nil {
		return false
	}
	if compare(s, t) {
		return true
	}
	return traverse(s.Left, t) || traverse(s.Right, t)
}

func compare(s, t *TreeNode) bool {

	if s == nil && t == nil {
		return true
	}
	if s == nil || t == nil {
		return false
	}
	if s.Val != t.Val {
		return false
	}
	return compare(s.Left, t.Left) && compare(s.Right, t.Right)
}
func main() {
	input := []int{1, 2, 2, 3, 4, 4, 3}
	intput2 := []int{2, 4, 3}
	tree := makeTree(input)
	subTree := makeTree(intput2)
	res := isSubtree(tree, subTree)
	fmt.Println(res)

}

func makeTree(input []int) *TreeNode {
	return getTree(0, input)
}
func getTree(subRootIndex int, input []int) *TreeNode {
	if subRootIndex >= len(input) || input[subRootIndex] == -1 {
		return &TreeNode{}
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
