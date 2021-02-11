// https://leetcode.com/problems/climbing-stairs/
// 70. Climbing Stairs
package main

import "fmt"

func main()  {
	res := climbStairsBottomUp(10)
	res2 := climbStairsTopDown(10)
	fmt.Println(res,res2)
}
func climbStairsBottomUp(n int) int {
	a := make([]int,n+1)
	if n < 3 {
		return n
	}

	for i:=0;i<=n;i++ {
		if i < 3 {
			a[i] = i
		} else {
			a[i] = a[i-1] + a[i-2]
		}
	}
	return a[n]
}
func climbStairsTopDown(n int) int {
	memo := make([]int,n)
	return calculate(0,n,memo)
}
func calculate(curr,n int,memo []int) int {
	if memo[curr] != 0 {
		return memo[curr]
	}
	if curr >= n {
		return 0
	}
	if curr == n-1 {
		return 1
	}
	if curr == n-2 {
		return 2
	}
	memo[curr] = calculate(curr+1,n,memo) + calculate(curr+2,n,memo)
	return memo[curr]
}