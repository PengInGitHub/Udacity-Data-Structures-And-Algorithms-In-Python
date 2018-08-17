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
        

def quickSortNew(aList):
    if len(aList) > 1:
        less, equal, greater = [], [], []
        pivot = aList[-1]
        for i in aList:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        return quickSortNew(less) + equal + quickSortNew(greater)

    return aList

test = [21, -4, -1, -1, 0, 900, 25, 6, 21, 14]
sortedList= quickSortNew(test)
print sortedList