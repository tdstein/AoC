package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Box [3][3]int

func (b Box) AdjacentRolls() int {
	sum := 0
	for i := range 3 {
		for j := range 3 {
			if i == 1 && j == 1 {
				// skip center
				continue
			}
			sum += b[i][j]
		}
	}
	return sum
}

type Grid [][]int

func (g Grid) GetBox(i, j int) Box {
	var box Box

	m := g.m()
	n := g.n()

	for di := -1; di <= 1; di++ {
		for dj := -1; dj <= 1; dj++ {
			r := i + di
			c := j + dj

			bi := di + 1 // map -1,0,1 → 0,1,2
			bj := dj + 1

			if r >= 0 && r < m && c >= 0 && c < n {
				box[bi][bj] = g[r][c]
			} else {
				box[bi][bj] = 0 // or any default value
			}
		}
	}

	return box
}

func (g Grid) m() int {
	return len(g)
}

func (g Grid) n() int {
	if len(g) > 0 {
		return len(g[0])
	}
	return 0
}

func main() {

	filename := "4.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	i := 0
	var grid Grid
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		grid = append(grid, make([]int, 0))
		for s := range strings.SplitSeq(scanner.Text(), "") {
			if s == "@" {
				grid[i] = append(grid[i], 1)
			} else {
				grid[i] = append(grid[i], 0)
			}
		}
		i++
	}

	result := 0
	for i, row := range grid {
		for j, _ := range row {
			if grid[i][j] != 1 {
				continue
			}

			box := grid.GetBox(i, j)
			rolls := box.AdjacentRolls()
			if rolls < 4 {
				result++
			}
		}
	}

	fmt.Println(result)
}
