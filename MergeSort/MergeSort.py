#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       print "mid: ", mid
       lefthalf = alist[:mid]#first half
       righthalf = alist[mid:]#second half

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               print "lefthalf[",i,"] < righthalf[",j,"]"
               print "lefthalf[i]:", lefthalf[i], "righthalf[j]", righthalf[j]
               print "aList before: ", alist 

               alist[k]=lefthalf[i]
               i=i+1
               print "aList after: ", alist 

           else:
               print "lefthalf[",i,"] >= righthalf[",j,"]", lefthalf[i], righthalf[j]
               print "aList before: ", alist               
               alist[k]=righthalf[j]
               j=j+1
               print "aList after: ", alist 
           k=k+1

       while i < len(lefthalf):
           print i, "<", len(lefthalf)
           print "aList before: ", alist               
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1
           print "aList after: ", alist 

       while j < len(righthalf):
           print "j < len(righthalf)", j, len(righthalf)
           print "aList before: ", alist 
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
           print "aList after: ", alist 
        

   print("Merging(alist) has only one element now ",alist)

alist = [54,26,93,17,77,31,44,55,20]
#mergeSort(alist)

def mergeSortNew(seq):
    if len(seq)<=1:
        return seq
    mid=int(len(seq)/2)
    left=mergeSortNew(seq[:mid])
    right=mergeSortNew(seq[mid:])
    return mergeNew(left, right)

def mergeNew(left, right):
    i, j = 0, 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1#donot forget this
        else:
            result.append(right[j])
            j+=1#donot forget this
    result+=left[i:]
    result+=right[j:]
    return result

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result


def mergeSortUpdate(aList):
    length = len(aList)
    if length<2:
        return aList
    mid = length/2
    left = mergeSortUpdate(aList[:mid])
    right = mergeSortUpdate(aList[mid:])

    return mergeUpdate(left, right)

def mergeUpdate(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result


merged = mergeSortUpdate(alist)
print(merged)       
    
