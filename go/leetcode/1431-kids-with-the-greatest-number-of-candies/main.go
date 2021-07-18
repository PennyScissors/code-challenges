package main

import (
	"fmt"
	"log"
)

func max(arr []int) (int, error) {
	if len(arr) <= 0 {
		return -1, fmt.Errorf("Empty array")
	}
	max := arr[0]
	for _, num := range arr {
		if num > max {
			max = num
		}
	}
	return max, nil
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	result := make([]bool, len(candies))
	if max, err := max(candies); err == nil {
		for i, num := range candies {
			if num+extraCandies >= max {
				result[i] = true
			}
		}
	}

	return result
}

func main() {
	log.Println(kidsWithCandies([]int{4, 2, 1, 1, 2}, 1))
	log.Println(kidsWithCandies([]int{2, 3, 5, 1, 3}, 3))
	log.Println(kidsWithCandies([]int{1, 3}, 1))
	log.Println(kidsWithCandies([]int{3, 3}, 3))
}
