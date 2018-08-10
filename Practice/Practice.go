package main

import (
	"fmt"
)

func main() {
	//items2 := make([]string, 0)
	c := &Classy{}
	c.addItem("tophat")
	c.addItem("bowtie")
	c.addItem("jacket")
	c.addItem("monocle")
	fmt.Println(c.getClassiness())
	c.addItem("bowtie")
	fmt.Println(c.getClassiness())
}

//Classy is interchangable with "fancy".
//If you add fancy-looking items, you will increase your "classiness".
type Classy struct {
	items []string
}

func (c *Classy) getClassiness() int {
	classinessCounter := 0
	if len(c.items) > 0 {
		for _, item := range c.items { //use := instead of in
			if item == "tophat" {
				classinessCounter += 2
			}
			if item == "bowtie" {
				classinessCounter += 4
			}
			if item == "monocle" {
				classinessCounter += 5
			}
		}
		return classinessCounter
	}
	return classinessCounter
}

func (c *Classy) addItem(newItem string) {
	c.items = append(c.items, newItem)
}
