package main

import (
	"fmt"
)

func main() {
	//create instance: https://gobyexample.com/structs
	// # Test store edge case
	h := *new(hashTable)
	fmt.Println(h.lookup("UDACIOUS"))
	h.store("UDACIOUS")
	h.store("UDACITY")
	fmt.Println(h.lookup("UDACIOUS"))
	fmt.Println(h.table[h.calculateHashValue("UDACIOUS")])
}

type hashTable struct {
	table [10000][]string
}

func (h *hashTable) store(input string) {
	hv := h.calculateHashValue(input)
	if hv != -1 {
		//if the string already exists
		if len(h.table[hv]) != 0 {
			h.table[hv] = append(h.table[hv], input)
		} else {
			h.table[hv] = []string{input}
		}
	}
}

func (h *hashTable) lookup(input string) int {
	hv := h.calculateHashValue(input)
	if hv != -1 {
		//if the string already exists
		if h.table[hv] != nil {
			return hv
		}
	}
	return -1
}

func (h *hashTable) calculateHashValue(input string) int {
	if len(input) >= 2 {
		return int([]rune(input)[0]*100) + int([]rune(input)[1])
	}
	return -1
}
