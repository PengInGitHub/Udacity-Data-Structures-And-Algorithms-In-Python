package main

import (
	"fmt"
)

func main() {
	//alist := []int{-54, 26, 93, 0, 77, 31, 44, 55, 1}
	alist2 := []int{0}
	sorted := mergeSort(alist2)
	fmt.Print(sorted)
}

func mergeSort(aList []int) []int {
	if len(aList) <= 1 {
		return aList
	}
	mid := int(len(aList) / 2)
	left := mergeSort(aList[:mid])
	right := mergeSort(aList[mid:])
	return merge(left, right)
}

func merge(left, right []int) []int {
	i, j := 0, 0
	result := make([]int, 0)
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}
	//concatenate slices
	//https://stackoverflow.com/questions/16248241/concatenate-two-slices-in-go
	result = append(result, left[i:]...)
	result = append(result, right[j:]...)
	return result
}
