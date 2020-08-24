package main

import (
	"fmt"
	"math"
)

// solving using bottom-up(tabulation) dp approach
func coinChange(coins []int, amount int) int {
	tab := make([]int, amount+1)
	for i := range tab {
		tab[i] = -1
	}
	tab[amount] = 0
	for i := amount; i >= 0; i-- {
		for _, coin := range coins {
			if i-coin >= 0 && tab[i] != -1 {

				currCoin := tab[i]
				if currCoin == -1 {
					currCoin = 0
				}
				c2 := tab[i-coin]
				if c2 == -1 {
					c2 = 999
				}
				tab[i-coin] = int(math.Min(float64(c2), float64(currCoin+1)))
			}
		}
	}
	return tab[0]
}
func main() {
	type CoinChange struct {
		coins  []int
		amount int
		result int
	}

	cases := []CoinChange{
		{
			coins:  []int{1, 2, 5},
			amount: 11,
			result: 3,
		},
		{
			coins:  []int{1, 7, 9},
			amount: 21,
			result: 3,
		},
		{
			coins:  []int{2},
			amount: 3,
			result: -1,
		},
	}

	for _, c := range cases {
		res := coinChange(c.coins, c.amount)
		successString := "Passed"
		if c.result != coinChange(c.coins, c.amount) {
			successString = "Failed"
		}

		fmt.Printf("%s - Test case for coins:%v amount:%d\t| Expected %d - found %d \n", successString, c.coins, c.amount, c.result, res)
	}

}
