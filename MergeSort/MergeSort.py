#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               print "lefthalf[i] < righthalf[j]", i, j
               print "lefthalf[i]", lefthalf[i], "righthalf[j]", righthalf[j]
               alist[k]=lefthalf[i]
               i=i+1
           else:
               print "lefthalf[i] >= righthalf[j]", i, j, lefthalf[i], righthalf[j]
               
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           print "i < len(lefthalf)", i, len(lefthalf),lefthalf
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           print "j < len(righthalf)", j, len(righthalf)
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging(alist) has only one element now ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)