// https://leetcode.com/problems/employee-importance/
// 690. Employee Importance
package main

import "fmt"

//Definition for Employee.
type Employee struct {
	Id           int
	Importance   int
	Subordinates []int
}

func getImportance(employees []*Employee, id int) int {
	empMap := make(map[int]*Employee)
	for i := 0; i < len(employees); i++ {
		empMap[employees[i].Id] = employees[i]
	}

	return getImportanceRecursion(empMap, id)
}
func getImportanceRecursion(employees map[int]*Employee, id int) int {
	employee := employees[id]
	sum := employee.Importance
	for i := 0; i < len(employee.Subordinates); i++ {
		sum += getImportanceRecursion(employees, employee.Subordinates[i])
	}
	return sum
}
func main() {
	//[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
	input := []*Employee{
		&Employee{
			Id:           1,
			Importance:   5,
			Subordinates: []int{2, 3},
		},
		&Employee{
			Id:           2,
			Importance:   3,
			Subordinates: []int{},
		},
		&Employee{
			Id:           3,
			Importance:   3,
			Subordinates: []int{},
		},
	}
	id := 1
	res := getImportance(input, id)
	fmt.Println(res)
}
