// https://leetcode.com/problems/sum-of-left-leaves/
// 404. Sum of Left Leaves
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
func sumOfLeftLeaves(root *TreeNode) int {
	return traverseAndAdd(root)
}
func traverseAndAdd(root *TreeNode) int {
	if root == nil {
		return 0
	}
	sum := traverseAndAdd(root.Right) + traverseAndAdd(root.Left)
	if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
		sum += root.Left.Val
	}
	return sum
}

func main() {
	input := []int{1, 2, 2, 3, 4, 4, 3}
	tree := makeTree(input)
	res := sumOfLeftLeaves(tree)
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
