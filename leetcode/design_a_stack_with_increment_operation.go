// https://leetcode.com/problems/design-a-stack-with-increment-operation/
// 1381. Design a Stack With Increment Operation
package main

import "fmt"

type CustomStack struct {
	stack []int
	top   int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{
		stack: make([]int, maxSize),
		top:   -1,
	}
}

func (this *CustomStack) Push(x int) {
	if (*this).top < len((*this).stack)-1 {
		(*this).top++
		(*this).stack[(*this).top] = x
	}

}

func (this *CustomStack) Pop() int {
	if (*this).top >= 0 {
		t := (*this).stack[(*this).top]
		(*this).top--
		return t
	}
	return -1

}

func (this *CustomStack) Increment(k int, val int) {
	for i := 0; i < len((*this).stack) && i < k; i++ {
		(*this).stack[i] += val
	}
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */

func main() {
	commands := []string{"CustomStack", "push", "push", "pop", "push", "push", "push", "increment", "increment", "pop", "pop", "pop", "pop"}
	values := [][]int{{3}, {1}, {2}, {}, {2}, {3}, {4}, {5, 100}, {2, 100}, {}, {}, {}, {}}
	res := []int{}
	var obj CustomStack
	for i, command := range commands {
		switch command {
		case "CustomStack":
			obj = Constructor(values[i][0])
			res = append(res, -2)

		case "push":
			obj.Push(values[i][0])
			res = append(res, -2)
		case "pop":
			res = append(res, obj.Pop())
		case "increment":
			obj.Increment(values[i][0], values[i][1])
			res = append(res, -2)
		}

	}
	fmt.Println(res)
}
