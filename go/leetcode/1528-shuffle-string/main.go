package main

import (
	"fmt"
)

func restoreString(s string, indices []int) string {
	result := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		result[indices[i]] = s[i]
	}
	return string(result)
}

func main() {
	fmt.Println(restoreString("art", []int{1, 0, 2}))
	fmt.Println(restoreString("aaiougrt", []int{4, 0, 2, 6, 7, 3, 1, 5}))
	fmt.Println(restoreString("codeleet", []int{4, 5, 6, 7, 0, 2, 1, 3}))
}
