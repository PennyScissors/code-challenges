package main

//"G()(al)" -> "Goal"

import "strings"

func interpret(command string) string {
	command = strings.Replace(command, "()", "o", -1)
	command = strings.Replace(command, "(al)", "al", -1)

	return command
}

func main() {
	println(interpret("G()(al)"))
}
