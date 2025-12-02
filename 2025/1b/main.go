package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
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

	path := filepath.Join(filename)
	f, err := os.Open(path)
	check(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()

		var direction rune
		var ticks int
		_, err := fmt.Sscanf(line, "%c%d", &direction, &ticks)
		check(err)

		for ticks > 0 {
			ticks--

			if direction == 'R' {
				position += 1
			} else {
				position -= 1
			}

			if position == 100 {
				position = 0
			}

			if position == 0 {
				password += 1
			}

			if position == -1 {
				position = 99
			}
		}
	}

	fmt.Println(password)
}
