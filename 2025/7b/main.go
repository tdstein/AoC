package main

import (
	"bufio"
	"os"
	"slices"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	filename := "7.sample"
	filename = "7.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	result := 0
	scanner := bufio.NewScanner(f)

	var xs []int
	for scanner.Scan() {
		line := scanner.Text()
		s := strings.Split(line, "")

		if xs == nil {
			xs = make([]int, len(s))
			i := slices.Index(s, "S")
			xs[i] = 1
			continue
		}

		if slices.Contains(s, "^") {
			for i, x := range xs {
				if x >= 1 {
					if s[i] == "^" {
						xs[i-1] = xs[i-1] + x
						xs[i] = 0
						xs[i+1] = xs[i+1] + x
					}
				}
			}
		}
	}

	for _, x := range xs {
		if x > 0 {
			result += x
		}
	}

	println(result)
}
