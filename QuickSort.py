"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) > 1:
        pivot = array[-1]
        less = []
        equal = []
        greater = []
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)                
            else:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:     
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
