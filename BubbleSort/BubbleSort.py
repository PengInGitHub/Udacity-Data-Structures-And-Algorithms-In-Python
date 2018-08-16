#https://www.pythoncentral.io/pythons-range-function-explained/
def bubbleSort(aList):
    #parameters for range func to generate broader loop index i
    start = len(aList) - 1
    #use len(aList)-1 instead of start = len(aList),
    #otherwise aList[j+1] would cause 'list index out of range'
    stop = 0
    step = -1 #each loop decrease by 1
   
    #broader loop
    print "array length: ", len(aList)
    for i in range(start, stop, step):
        #inner loop
        print "loop index i : ", i
        for j in range(i):
            print "innder index j: ", j
            if aList[j] > aList[j+1]:
                #swap
                print "before swap: aList[j]: aList[j+1]:", aList[j], aList[j+1]
                tmp = aList[j]
                aList[j] = aList[j+1]
                aList[j+1] = tmp
                print "after swap: aList[j]: aList[j+1]:", aList[j], tmp
        
def bubbleSortSolution(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                #swap
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def bubbleSortTest(aList):
  start = len(aList) - 1
  stop = 0
  step = -1
  #outer loop, index i
  for i in range(start, stop, step):
    #inner loop, index j
    for j in range(i):
      if aList[j] > aList[j+1]:
        #swap
        tmp = aList[j]
        aList[j] = aList[j+1]
        aList[j+1] = tmp

aList = [54,26,93,17,77,31,44,55,20]
aList1 = [54,26,93,-17,77,0,44,55,20]
aList2 = [54]
aList3 = [0]
aList4 = [-1]

bubbleSort(aList)
bubbleSort(aList1)
bubbleSort(aList2)
bubbleSort(aList3)
bubbleSort(aList4)

print aList
print aList1
print aList2
print aList3
print aList4

aList = [103,54,26,93,0,17,77,1,17,31,44,55,20]
aList0 = [0]
aList1 = [1]
bubbleSort(aList0)
bubbleSort(aList1)
bubbleSort(aList)
print aList
print aList0
print aList1
