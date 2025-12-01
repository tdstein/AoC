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

	path := filepath.Join("..", "1.in")
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
