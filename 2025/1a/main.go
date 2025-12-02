package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	password := 0
	position := 50

	filename := "1.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()

		var direction rune
		var ticks int
		_, err := fmt.Sscanf(line, "%c%d", &direction, &ticks)
		check(err)

		if direction == 'R' {
			position = (position + ticks) % 100
		} else {
			position = (((position - ticks) % 100) + 100) % 100
		}

		if position == 0 {
			password += 1
		}
	}

	fmt.Println(password)
}
