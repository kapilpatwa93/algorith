// https://leetcode.com/problems/distribute-candies-to-people/
// 1103. Distribute Candies to People
package main

import "fmt"

func distributeCandies(candies int, numPeople int) []int {
	arr := make([]int, numPeople)
	round := 0
	i := 0
	for {
		if i == numPeople {
			round++
			i = 0
		}
		c := round*numPeople + i + 1
		if c > candies {
			c = candies
		}
		arr[i] += c
		candies -= c
		if candies <= 0 {
			break
		}
		i++
	}
	return arr

}
func main() {
	candies := 10
	numPeople := 4
	res := distributeCandies(candies, numPeople)
	fmt.Println(res)
}
