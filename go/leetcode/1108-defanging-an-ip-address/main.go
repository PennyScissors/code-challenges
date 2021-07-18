package main

import (
	"fmt"
	"strings"
)

func defangIPaddr1(address string) string {
	return strings.ReplaceAll(address, ".", "[.]")
}

func defangIPaddr(address string) string {
	var offset int
	for i, c := range address {
		if c == '.' {
			address = address[:i+offset] + "[.]" + address[i+1+offset:]
			offset += 2
		}
	}
	return address
}

func main() {
	fmt.Println(defangIPaddr("1.2.3.4.5"))
}
