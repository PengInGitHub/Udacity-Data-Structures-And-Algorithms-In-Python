package main

import (
	"fmt"
)

//https://gist.github.com/vderyagin/4161347

func main() {
	test := []int{21, -4, -1, -1, 0, 900, 25, 6, 21, 14}
	quickSorted := quickSortNew(test)
	fmt.Println(quickSorted)
}

func quickSort(aList []int) []int {
	if len(aList) < 2 {
		return aList
	}

	less, equal, greater := make([]int, 0), make([]int, 0), make([]int, 0)
	//take the last element in slice
	//python: pivot = aList[-1]
	//golang: pivot := aList[len(aList)-1]
	//java: pivot = aList[aList.length-1] if aList is of type int[]
	//		pivot = aList.get(aList.size() - 1)
	pivot := aList[len(aList)-1]
	for _, i := range aList {
		if i < pivot {
			less = append(less, i)
		} else if i == pivot {
			equal = append(equal, i)
		} else {
			greater = append(greater, i)
		}
	}
	//concatenate multiple slice
	//python: result = less + equal + greater
	//golang: result = append(less, equal...)
	//		  result = append(result, greater...)

	less, greater = quickSort(less), quickSort(greater)
	result := append(less, equal...)
	return append(result, greater...)
}

func quickSortNew(aList []int) []int {
	length := len(aList)
	if length < 2 {
		return aList
	}

	//cause error
	//	less, equal, greater := make([]int, length), make([]int, length), make([]int, length)
	less, equal, greater := make([]int, 0), make([]int, 0), make([]int, 0)
	pivot := aList[length-1]

	for _, x := range aList {
		if x < pivot {
			less = append(less, x)
		} else if x == pivot {
			equal = append(equal, pivot)
		} else {
			greater = append(greater, pivot)
		}
	}
	//infinite loop
	//result := append(quickSortNew(less), equal...)
	//result = append(result, quickSortNew(greater)...)
	less, greater = quickSortNew(less), quickSortNew(greater)
	result := append(less, equal...)
	return append(result, greater...)
}
