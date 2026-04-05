import numpy as np
import pandas as pd

def mergeSort(array):
    inputLength = len(array)

    if inputLength < 2:
        return

    midIndex = inputLength // 2
    leftArray = np.empty(midIndex, dtype='int')
    rightIndex = inputLength - midIndex
    rightArray = np.empty(rightIndex, dtype='int')

    for i in range(midIndex):
        leftArray[i] = array[i]

    for i in range(midIndex, inputLength):
        rightArray[i - midIndex] = array[i]


    mergeSort(leftArray)
    mergeSort(rightArray)
    merge(array, leftArray, rightArray)
#    return array


def merge(array, leftArray, rightArray):
    leftLength = len(leftArray)
    rightLength = len(rightArray)

    #need 3 iterators
    i = j = k = 0

    while(i < leftLength and j < rightLength):
        #Element in left array less than element in right array
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            #Element in right array is the smaller
            array[k] = rightArray[j]
            j += 1
        #increment the input array
        k += 1
    
    #need to take care of the remaining elements
    #left array
    while (i < leftLength):
        array[k] = leftArray[i]
        i += 1
        k += 1
    
    #right array 
    while (j < rightLength):
        array[k] = rightArray[j]
        j += 1
        k += 1

def threeWayMergeSort(array):
    arrayLength = len(array)
    chunks = arrayLength //3
    chunksLeft = arrayLength % 3

    leftArray = np.empty(chunks, dtype='int')
    midArray = np.empty(chunks, dtype='int')
    if chunksLeft != 0:
        newChunks = chunks + chunksLeft
        rightArray = np.empty(newChunks, dtype='int')
    else:
        rightArray = np.empty(chunks, dtype='int')


    for i in range(chunks):
        leftArray[i] = array[i]

    for i in range(chunks, chunks * 2):
        midArray[i - chunks] = array[i]
    
    for i in range(chunks * 2, arrayLength):
        rightArray[i - (chunks * 2)] = array[i]

    newArray = np.zeros(len(leftArray) + len(midArray), dtype='int')
    merge(newArray, leftArray, midArray)
    mergeSort(newArray)
    merge(array, newArray, rightArray)
    mergeSort(array)


