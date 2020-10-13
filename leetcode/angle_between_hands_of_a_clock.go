// https://leetcode.com/problems/angle-between-hands-of-a-clock
// 1344. Angle Between Hands of a Clock
package main

import (
	"fmt"
	"math"
)

func angleClock(hour int, minutes int) float64 {
	if hour == 12 {
		hour = 0
	}
	hoursBase := float64(30*hour)
	hourRelative := float64(30) * float64(minutes)/float64(60)
	hrs := hoursBase + hourRelative
	mins := (float64(minutes) / float64(60)) * 360
	res := math.Abs(hrs - mins)
	if res > 180 {
		return 360 - res
	}
	return res
}
func main() {
	hour := 4
	minutes := 50
	res := angleClock(hour,minutes)
	fmt.Println(res)
}
