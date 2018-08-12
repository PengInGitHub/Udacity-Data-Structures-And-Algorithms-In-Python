"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    lowIndex = 0
    highIndex = len(input_array) - 1
    while lowIndex <= highIndex:
        medianIndex = (lowIndex+highIndex) / 2
        if input_array[medianIndex] == value:
            return medianIndex       
        elif input_array[medianIndex] < value:
            lowIndex = medianIndex + 1
        else:
            highIndex = medianIndex - 1
    return -1
            
test_list = [1,3,9,11,15,19,29]
test_val1 = 25#-1
test_val2 = 15#4
test_val3 = 1#0
test_val4 = 29#6
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)
print binary_search(test_list, test_val4)