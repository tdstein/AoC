package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func transpose[E any](xs [][]E, M, N int, fill E) [][]E {
	ys := make([][]E, N)
	for i := range N {
		ys[i] = make([]E, M)
	}

	for i := range M {
		for j := range N {
			if i >= len(xs) || j >= len(xs[i]) {
				ys[j][i] = fill
			} else {
				ys[j][i] = xs[i][j]
			}
		}
	}

	return ys
}

func split[T any](xs []T, pred func(T) bool) [][]T {
	var out [][]T
	var cur []T

	for _, x := range xs {
		if pred(x) {
			if len(cur) > 0 {
				out = append(out, cur)
			}
			cur = []T{}
			continue
		}
		cur = append(cur, x)
	}

	if len(cur) > 0 {
		out = append(out, cur)
	}

	return out
}

func sum(xs []int) int {
	n := 0
	for _, v := range xs {
		n += v
	}
	return n
}

func product(xs []int) int {
	n := 1
	for _, v := range xs {
		n *= v
	}
	return n
}

func main() {

	filename := "6.sample"
	// filename = "6.in"

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	var M, N int
	var xs [][]string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		x := strings.Split(line, "")
		xs = append(xs, x)
		N = max(N, len(x))
		M++
	}

	l := len(xs) - 1
	v := xs[l]
	ops := strings.Fields(strings.Join(v, ""))

	xs = xs[:l]
	xs = transpose(xs, M, N, " ")

	// split each group by empty columns
	ys := split(xs, func(x []string) bool {
		s := strings.TrimSpace(strings.Join(x, ""))
		return s == ""
	})

	// convert [[[1      ] [2 4    ] [3 5 6  ]], ...] into [[1, 23, 356], ...]
	var zs [][]int
	for _, y := range ys {
		var z []int
		for _, s := range y {
			s := strings.TrimSpace(strings.Join(s, ""))
			v, err := strconv.Atoi(s)
			check(err)

			z = append(z, v)
		}
		zs = append(zs, z)
	}

	result := 0
	for i, op := range ops {
		if op == "+" {
			result += sum(zs[i])
		}
		if op == "*" {
			result += product(zs[i])
		}
	}

	println(result)
}
