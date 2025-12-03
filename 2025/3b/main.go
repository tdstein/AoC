package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Converts an array of integers into a single number
//
// For example:
//
//	[1, 2, 3] => 123
//	[0, 0, 0] => 0
//	[0, 0, 1] => 1
func toInt(ints []int) int {
	n := 0
	for _, d := range ints {
		if d > 9 {
			panic("digit out of range")
		}
		n = (n * 10) + d
	}
	return n
}

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

		var bank []int
		for s := range strings.SplitSeq(scanner.Text(), "") {
			v, err := strconv.Atoi(s)
			check(err)

			bank = append(bank, v)
		}

		// take the first 12, then iterate over the rest
		jolts, bank := bank[:12], bank[12:]
		for i := 0; i < len(bank); i++ {
			// append next number as a candidate
			jolts = append(jolts, bank[i])
			for j := range 12 {
				if jolts[j] < jolts[j+1] {
					// If the element is lower than it's neighbor, remove it, then break to the next candidate
					jolts = append(jolts[:j], jolts[j+1:]...)
					break
				}
			}
			// only keep 12 digits
			jolts = jolts[:12]
		}

		result += toInt(jolts)
	}
	fmt.Println(result)
}
