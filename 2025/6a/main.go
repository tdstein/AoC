package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	filename := "6.sample"
	filename = "6.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	result := 0

	var xss [][]int
	var ops []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		s := strings.Fields(line)
		if s[0] == "+" || s[0] == "*" {
			ops = s
			continue
		}

		var xs []int
		for _, v := range s {
			x, err := strconv.Atoi(v)
			check(err)

			xs = append(xs, x)
		}
		xss = append(xss, xs)
	}

	for j, op := range ops {
		var n int
		if op == "*" {
			n = 1
		}
		if op == "+" {
			n = 0
		}

		for i := range xss {
			if op == "*" {
				n *= xss[i][j]
			}
			if op == "+" {
				n += xss[i][j]
			}
		}

		result += n
	}
	fmt.Println(result)
}
