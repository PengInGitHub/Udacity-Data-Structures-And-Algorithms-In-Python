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


def bulleSortUpdate(aList):
    length = len(aList)
    
    if length < 2:
        return aList
    
    start = length-1#mistake made, should be length-1 instead of length
    stop = 0
    step = -1

    #outter loop, i would be ... 3, 2, 1
    for i in range(start, stop, step):
        #inner loop from 0 to the value of i
        for j in range(i):
            if aList[j] > aList[j+1]:
                #swap
                tmp = aList[j]
                aList[j] = aList[j+1]
                aList[j+1] = tmp
    return aList
aList = [54,-17,26,93,-17,77,0,0,44,55,20]

updated = bulleSortUpdate(aList)

print updated

