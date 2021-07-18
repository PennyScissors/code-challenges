package main

import "fmt"

func shuffle(nums []int, n int) []int {
	var result []int
	for i := 0; i < n; i++ {
		result = append(result, nums[i], nums[i+n])
	}
	return result
}

func main() {
	fmt.Println(shuffle([]int{1, 2, 3, 11, 22, 33}, 3))
	fmt.Println(shuffle([]int{1, 1, 2, 2}, 2))
	fmt.Println(shuffle([]int{1, 2, 3, 4, 4, 3, 2, 1}, 4))
}
