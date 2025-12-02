package main

import (
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

// https://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python
func invalid(s string) bool {
	n := len(s)
	doubled := s + s
	return strings.Contains(doubled[1:((2*n)-1)], s)
}

func main() {

	filename := "2.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	dat, err := os.ReadFile(filename)
	check(err)

	str := string(dat)
	str = strings.TrimSpace(str)

	ranges := strings.Split(str, ",")

	total := 0
	for _, v := range ranges {
		v := strings.Split(v, "-")

		a := v[0]
		b := v[1]

		i, err := strconv.Atoi(a)
		check(err)

		j, err := strconv.Atoi(b)
		check(err)

		for i <= j {
			a := strconv.Itoa(i)
			if invalid(a) {
				total += i
			}
			i++
		}
	}

	fmt.Println(total)
}
