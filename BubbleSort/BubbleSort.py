#https://www.pythoncentral.io/pythons-range-function-explained/
def bubbleSort(aList):
    #parameters for range func to generate broader loop index i
    start = len(aList) - 1
    stop = 0
    step = -1 #each loop decrease by 1
   
    #broader loop
    for i in range(start, stop, step):
        #inner loop
        for j in range(i):
            if aList[j] > aList[j+1]:
                #swap
                tmp = aList[j]
                aList[j] = aList[j+1]
                aList[j+1] = tmp
        
def bubbleSortSolution(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                #swap
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

aList = [103,54,26,93,0,17,77,1,17,31,44,55,20]
aList0 = [0]
aList1 = [1]
bubbleSort(aList0)
bubbleSort(aList1)
bubbleSort(aList)
print aList
print aList0
print aList1
