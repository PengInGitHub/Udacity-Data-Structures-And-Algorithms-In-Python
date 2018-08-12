package main

import (
	"fmt"
	"sort"
)

func main() {
	locations := make(continentNation)
	locations["Asia"] = cityNation{"China": {"Beijing", "Shanghai"}}
	locations["North America"] = cityNation{"USA": {"Mountain View"}}
	locations["North America"]["USA"] = append(locations["North America"]["USA"], "Atlanta")
	locations["Asia"]["India"] = append(locations["North America"]["India"], "Bangalore")
	locations["Africa"] = cityNation{"Egypt": {"Cairo"}}
	//Q1
	usCities := locations["North America"]["USA"]
	sort.Slice(usCities, func(i, j int) bool {
		return usCities[i] < usCities[j]
	})
	fmt.Println(1)
	for _, usCity := range usCities {
		fmt.Println(usCity)
	}

	//Q2
	var citiesNationPairs []string
	for nation, cities := range locations["Asia"] {
		for _, city := range cities {
			citiyNationPairs := city + " - " + nation
			citiesNationPairs = append(citiesNationPairs, citiyNationPairs)
		}
	}
	sort.Slice(citiesNationPairs, func(i, j int) bool {
		return citiesNationPairs[i] < citiesNationPairs[j]
	})
	fmt.Println(2)
	for _, cityNationPairs := range citiesNationPairs {
		fmt.Println(cityNationPairs)
	}
}

type cityNation map[string][]string
type continentNation map[string]cityNation
