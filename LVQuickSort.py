#QuickSort Las Vegas

import random

counter = 0
def LVQuickSort(listToSort):
    quickSort(listToSort,0,len(listToSort)-1)
    
def quickSort(listToSort, start , end): 
    if(start < end): 
        indexPiv = randomizePartition(listToSort, start, end)
        quickSort(listToSort , start , indexPiv - 1) 
        quickSort(listToSort, indexPiv + 1, end) 
  
def randomizePartition(listToSort , start, end): 
    
    randpivot = random.randrange(start, end) #Randomizing the index
    listToSort[start], listToSort[randpivot] = listToSort[randpivot], listToSort[start] #Switching the first elem with the pivot elem
    return inPlacePartition(listToSort, start, end) 
  
def inPlacePartition(listToSort,start,end): 
    lastMinElem = start + 1  #Set where the partition start
    pivot = start            #Set a meaningful name to the pivot at the start of the sub-sequence/sequence
    global counter
    for i in range(start + 1, end + 1): 
        counter = counter + 1
        if listToSort[i] <= listToSort[pivot]: 
            listToSort[lastMinElem] , listToSort[i] = listToSort[i] , listToSort[lastMinElem] 
            lastMinElem = lastMinElem + 1
    listToSort[pivot] , listToSort[lastMinElem - 1] = listToSort[lastMinElem - 1] , listToSort[pivot] 
    indexToReturn = lastMinElem - 1
    return (indexToReturn) 

def createTheSequenceRand(listToFill,numberOfElem):
    
    for i in range(1, numberOfElem+1): #Fill the sequence with all different numbers
        listToFill.append(i)

    random.shuffle(listToFill) #Shuffling the sequence
  

#Where the experiments start
if __name__ == "__main__": 
    
    listOf10K = []

    createTheSequenceRand(listOf10K,10000)#Creating the sequence

    numberOfRuns = []

    listOfCounts10K = []
    for j in range(1,10001):
        listToSort = listOf10K
        numberOfRuns.append(j)
        LVQuickSort(listToSort)
        listOfCounts10K.append(counter)
        counter = 0                     #Setting the counter at zero for the next run
        

    f = open("output10K.txt","w+")

    for i in listOfCounts10K: #Setting an output file
	    f.write(str(i) + "\n")
   
    listOf1M = []

    createTheSequenceRand(listOf1M,1000000)#Creating the sequence

    listOfCounts1M = []
    for j in range(1,1001):
        listToSort = listOf1M
        LVQuickSort(listToSort)
        listOfCounts1M.append(counter)
        counter = 0                     #Setting the counter at zero for the next run
        

    f = open("output1M.txt","w+")

    for i in listOfCounts1M: #Setting an output file
	    f.write(str(i) + "\n")

    