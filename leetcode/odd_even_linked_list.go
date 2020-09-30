// https://leetcode.com/problems/odd-even-linked-list
// 328. Odd Even Linked List
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
func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	odd := head
	oPtr := odd
	even := head.Next
	ePtr := even
	head = even.Next
	counter := 0
	for ; head != nil; {
		if counter%2 == 0 {
			oPtr.Next = head
			oPtr = oPtr.Next

		} else {
			ePtr.Next = head
			ePtr = ePtr.Next
		}
		counter++
		head = head.Next
	}

	if counter%2 == 1 {
		ePtr.Next = nil
	} else {
		oPtr.Next = nil
	}
	oPtr.Next = even
	return odd
}
func main() {
	b := []int{1, 2, 4, 5, 6, 7}
	head := makeLinkedList(b, nil)
	res := oddEvenList(head)
	fmt.Println(res)

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
