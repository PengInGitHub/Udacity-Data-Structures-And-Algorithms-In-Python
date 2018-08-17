package main

import (
	"fmt"
)

func main() {
	test := []int{21, -4, -1, -1, 0, 900, 25, 6, 21, 14}
	mergeSorted := mergeSort(test)
	fmt.Println(mergeSorted)
}

func mergeSort(aList []int) []int {
	if len(aList) < 2 {
		return aList
	}

	less, equal, greater := make([]int, 0), make([]int, 0), make([]int, 0)
	//take the last element in slice
	//python: pivot = aList[-1]
	//golang: pivot := aList[len(aList)-1]
	//java: pivot = aList[aList.length-1]
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

	less, greater = mergeSort(less), mergeSort(greater)
	result := append(less, equal...)
	return append(result, greater...)
}
