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

	filename := "3.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	result := 0
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		var bank []int = make([]int, len(line))
		for i, s := range strings.Split(line, "") {
			v, err := strconv.Atoi(s)
			check(err)

			bank[i] = v
		}

		var first int
		for i, v := range bank[:len(bank)-1] {
			if v > bank[first] {
				first = i
			}
		}

		var second int = first + 1
		for i := second; i < len(bank); i++ {
			v := bank[i]
			if v > bank[second] {
				second = i
			}
		}

		result += (bank[first]*10 + bank[second])
	}

	fmt.Println(result)
}
