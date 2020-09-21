// https://leetcode.com/problems/intersection-of-two-linked-lists/
// 160. Intersection of Two Linked Lists
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}
	p1 := headA
	p2 := headB
	nullCount := 0
	for {
		if p1 == p2 {
			return p1
		}
		if p1.Next == nil {
			nullCount++
			p1 = headB
		} else {
			p1 = p1.Next
		}
		if p2.Next == nil {
			nullCount++
			p2 = headA
		} else {
			p2 = p2.Next
		}
		if nullCount > 2 {
			return nil
		}
	}
}

func main() {
	a := []int{2, 3, 4, 5}
	b := []int{1, 6, 7, 4, 5}
	skipA := 2
	rem := makeLinkedList(a[skipA:], nil)
	headA := makeLinkedList(a[:skipA], rem)
	skipB := 3
	headB := makeLinkedList(b[:skipB], rem)
	res := getIntersectionNode(headA, headB)
	fmt.Printf("%v", res.Val)

}

func makeLinkedList(arr []int, rem *ListNode) *ListNode {

	var p *ListNode
	for i := len(arr) - 1; i >= 0; i-- {
		head := ListNode{
			Val:  arr[i],
			Next: rem,
		}
		if p != nil {
			head.Next = p
		}
		p = &head
	}
	return p
}
