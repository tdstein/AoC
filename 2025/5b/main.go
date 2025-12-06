package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// https://algo.monster/liteproblems/56
func merge(xs [][]int) [][]int {
	var st, ed int
	st = xs[0][0]
	ed = xs[0][1]

	var ys [][]int
	for _, x := range xs {
		var s, e int
		s = x[0]
		e = x[1]

		if ed < s {
			ys = append(ys, []int{st, ed})
			st, ed = s, e
		} else {
			ed = max(ed, e)
		}
	}
	ys = append(ys, []int{st, ed})

	return ys
}

func main() {

	// filename := "5.sample"
	filename := "5.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	result := 0

	var xs [][]int
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}

		cs := strings.Split(line, "-")

		var a, b int
		a, err = strconv.Atoi(cs[0])
		check(err)
		b, err = strconv.Atoi(cs[1])
		check(err)

		xs = append(xs, []int{a, b})
	}

	sort.Slice(xs[:], func(i, j int) bool {
		return xs[i][0] < xs[j][0]
	})

	xs = merge(xs)

	for _, x := range xs {
		var s, e int
		s = x[0]
		e = x[1]

		result += e - s + 1
	}

	fmt.Println(result)
}
