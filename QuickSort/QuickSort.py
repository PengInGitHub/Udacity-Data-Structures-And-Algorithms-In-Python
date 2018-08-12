"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    #print "origin: ", array
    if len(array) > 1:
        pivot = array[-1]
        #print "pivot: ", pivot
        less, equal, greater = [], [], []
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)                
            else:
                greater.append(x)
        #combine three arrays 
        #print "less: ", less, "equal", equal, "greater", greater
        return quicksort(less) + equal + quicksort(greater)
    return array     
        

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)