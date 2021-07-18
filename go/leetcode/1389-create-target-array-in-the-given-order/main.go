package main

import "fmt"

func createTargetArray(nums []int, index []int) []int {
	var result []int
	for i, position := range index {
		if position != i {
			result = append(result[:position+1], result[position:]...)
			result[position] = nums[i]

		} else {
			result = append(result, nums[i])
		}
	}
	return result
}

func main() {
	fmt.Println(createTargetArray([]int{0, 1, 2, 3, 4}, []int{0, 1, 2, 2, 1}))
	fmt.Println(createTargetArray([]int{1}, []int{0}))
	fmt.Println(createTargetArray([]int{1, 2, 3, 4, 0}, []int{0, 1, 2, 3, 0}))
	fmt.Println(createTargetArray([]int{}, []int{}))
}
