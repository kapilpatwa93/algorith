// https://leetcode.com/problems/symmetric-tree/
// 101. Symmetric Tree
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

func isSymmetric(root *TreeNode) bool {
	res := true
	res = compare(root, root)
	return res
}
func compare(sRoot1 *TreeNode, sRoot2 *TreeNode) bool {
	if sRoot1 == nil && sRoot2 == nil {
		return true
	} else if sRoot1 == nil || sRoot2 == nil {
		return false
	} else if sRoot1.Val != sRoot2.Val {
		return false
	}
	return compare(sRoot1.Left, sRoot2.Right) && compare(sRoot1.Right, sRoot2.Left)
}

func main() {
	input := []int{1, 2, 2, 3, 4, 4, 3}
	tree := makeTree(input)
	res := isSymmetric(tree)
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
