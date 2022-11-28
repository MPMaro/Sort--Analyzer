# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")




# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")




#BubbleSort
def bubbleSort(anArray):
    
  for i in range(len(anArray)):

    for n in range(len(anArray) - i - 1):
        
      if anArray[n] > anArray[n + 1]:
        store = anArray[n]
        anArray[n] = anArray[n+1]
        anArray[n+1] = store

#SelectionSort
def selectionSort(anArray):
    for i in range(len(anArray)):
        minimum = i
        for n in range(i+1, len(anArray)):
            if anArray[n] < anArray[minimum]:
                minimum = n
        anArray[i], anArray[minimum] = anArray[minimum], anArray[i]

#InsertionSort
def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertion = anArray[i]
        n = i -1
        while n >= 0 and insertion < anArray[n]:
            anArray[n + 1] = anArray[n]
            n = n - 1
        anArray[n + 1] = insertion


#Run Sort
test = 3
storeTime = []
for i in range(test):
    startTime = time.time()
    function = insertionSort(reversedData)
    endTime = time.time()
    storeTime.append(endTime - startTime)

addTime = storeTime[0] + storeTime[1] + storeTime[2]
avgTime = addTime/test

print(f"The time is:\n{avgTime}")

