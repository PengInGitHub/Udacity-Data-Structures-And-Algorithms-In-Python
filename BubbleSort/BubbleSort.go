package main

import (
	"fmt"
)

func bubbleSortTest(aList []int) {
	for i := 1; i < len(aList); i++ {
		for j := 0; j < i; j++ {
			if aList[j] > aList[j+1] {
				//swap
				aList[j], aList[j+1] = aList[j+1], aList[j]
			}
		}
	}
}

func main() {
	aList := []int{103, -54, 26, 93, 0, -17, 77, 1, 17, 31, 44, 55, 20}
	bubbleSortTest(aList)
	fmt.Println(aList)
}

func bubbleSort(aSlice []int) {
	for i := len(aSlice) - 1; i > 0; i-- {
		for j := 0; j < i; j++ {
			if aSlice[j] > aSlice[j+1] {
				//swap
				aSlice[j], aSlice[j+1] = aSlice[j+1], aSlice[j]
			}
		}
	}
}
