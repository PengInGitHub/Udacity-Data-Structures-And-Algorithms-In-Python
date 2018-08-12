package main

import "fmt"

func main() {
	fmt.Println(getFibSlice(9))  //34
	fmt.Println(getFibSlice(11)) //89
	fmt.Println(getFibSlice(59)) //956722026041
	fmt.Println(getFibSlice(1))  //1
	fmt.Println(getFibSlice(2))  //1
	fmt.Println(getFibSlice(3))  //2
	fmt.Println(getFibSlice(0))  //0
}

func getFibSlice(p int) int {
	f := make([]int, p+2) //len should be p+1, but p+2 avoids panic in 'f[1] = 1' when p = 0
	f[0] = 0
	f[1] = 1
	var i int
	for i = 2; i <= p; i++ {
		f[i] = f[i-1] + f[i-2]
	}
	return f[p]
}

func getFib(p int) int {
	if p < 0 {
		return 0
	}
	if p <= 1 {
		return p
	}
	first, second := 0, 1
	next := first + second
	for i := 3; i <= p; i++ {
		first, second = second, next
		next = first + second
	}
	return next
}

//Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
func getFibRecursion(p int) int {
	if p == 0 || p == 1 {
		return p
	}
	return getFibRecursion(p-1) + getFibRecursion(p-2)
}
