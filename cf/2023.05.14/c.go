package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const modulus = 1000000000 + 7

func main() {
	in := bufio.NewReader(os.Stdin)
	tc := readInt(in)

	for t := 0; t < tc; t++ {
		n := readInt(in)
		a := readArrInt(in)
		b := readArrInt(in)
		sort.Sort(sort.Reverse(sort.IntSlice(a)))
		sort.Sort(sort.Reverse(sort.IntSlice(b)))
		i := 0
		res := 1
		for j := 0; j < n; j++ {
			for ; i < n && a[i] > b[j]; i++ {
			}
			res = (res * (i - j)) % modulus
		}
		fmt.Println(res)
	}
}

func readInt(in *bufio.Reader) int {
	nStr, _ := in.ReadString('\n')
	nStr = strings.ReplaceAll(nStr, "\r", "")
	nStr = strings.ReplaceAll(nStr, "\n", "")
	n, _ := strconv.Atoi(nStr)
	return n
}

func readLineNumbs(in *bufio.Reader) []string {
	line, _ := in.ReadString('\n')
	line = strings.ReplaceAll(line, "\r", "")
	line = strings.ReplaceAll(line, "\n", "")
	numbs := strings.Split(line, " ")
	return numbs
}

func readArrInt(in *bufio.Reader) []int {
	numbs := readLineNumbs(in)
	arr := make([]int, len(numbs))
	for i, n := range numbs {
		val, _ := strconv.Atoi(n)
		arr[i] = val
	}
	return arr
}

func readArrInt64(in *bufio.Reader) []int64 {
	numbs := readLineNumbs(in)
	arr := make([]int64, len(numbs))
	for i, n := range numbs {
		val, _ := strconv.ParseInt(n, 10, 64)
		arr[i] = val
	}
	return arr
}
