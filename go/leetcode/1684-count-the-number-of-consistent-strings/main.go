package main

import (
	"fmt"
	"strings"
)

func countConsistentStrings(allowed string, words []string) int {
	var count int
	allowedSet := make(map[rune]bool)

	for _, c := range allowed {
		allowedSet[c] = true
	}

	for _, w := range words {
		invalid := false
		for _, c := range w {
			if _, exists := allowedSet[c]; !exists {
				invalid = true
				break
			}
		}
		if !invalid {
			count++
		}
	}

	return count
}

func countConsistentStrings(allowed string, words []string) int {
	var count int
	for _, w := range words {
		for _, c := range strings.Split(allowed, "") {
			w = strings.ReplaceAll(w, c, "")
		}
		if len(w) == 0 {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(countConsistentStrings("abc", []string{"a", "b", "c", "ab", "ac", "bc", "abc"}))
	fmt.Println(countConsistentStrings("ab", []string{"ad", "bd", "aaab", "baa", "badab"}))
}
