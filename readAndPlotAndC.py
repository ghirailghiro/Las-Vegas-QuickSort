import matplotlib.pyplot as plt
import math

#Function for plot a Histogram with in input data and Bin
def plotHist(listOfData,binExp):
    plt.style.use('ggplot')
    plt.hist(listOfData, bins=binExp)
    plt.show()

#Function for read integer from file with in input a filename
def readDataFromF(filename):
    with open(filename) as f:
        content = f.readlines()

    listOfData = [int(x.strip()) for x in content]
    return listOfData 

#Calculating C constant in front of nlogn
def calculateC(listOfData,dimOfExp,numOfRuns):
    sumTot = 0
    for j in range(0,len(listOfData)):             #Sum of the j-runs
        sumTot += listOfData[j]

    sumTot = sumTot/numOfRuns       #Divided the Sum with the number of Runs
    C = sumTot /(dimOfExp*math.log(dimOfExp)) #calculating C
    return C



if __name__ == "__main__": 

    #Histograms for 10K elements
    filename= "output10K.txt"
    listOf10k= readDataFromF(filename)
    plotHist(listOf10k,1000)
    plotHist(listOf10k,100)
    plotHist(listOf10k,50)


    print(calculateC(listOf10k,10000,10000))

    #Histograms for 1M elements
    filename= "output1M.txt"
    listOf1M= readDataFromF(filename)
    plotHist(listOf1M,1000)
    plotHist(listOf1M,100)
    plotHist(listOf1M,50)



    print(calculateC(listOf1M,1000000,1000))


