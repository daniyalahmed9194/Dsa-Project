import math

# bubble sort
def bubbleSort (array, column):
    swapped = True # flag
    i = 0
    n = len(array) # length of array
    while swapped: # outer loop will break if array is already sorted
        swapped = False
        for j in range (n-i-1): # inner loop
            if array[j][column] > array[j+1][column]:  # sorting condition
                array[j], array[j+1] = array[j+1], array[j] # swapping
                swapped = True
        i = i + 1

    return array

# insertion sort
def insertionSort (array, column):
    n = len(array) # length of array
    for i in range(1, n):
        key = array[i] # key value to compare with all the sorted elements of previous array
        j = i - 1
        while j>=0 and array[j][column]>key[column]: # comparing values
            array[j+1] = array [j]
            j = j - 1
        
        array [j+1] = key
    return array

# selection sort
def selectionSort (array,column):
    arrayLength = len(array) # length of array
    for i in range (0, arrayLength - 1):
        min = i # index of minimum value in the array
        for j in range (i+1,arrayLength):
            if array[j][column] < array[min][column]: # comparison 
                min = j
        array[i], array[min] = array[min], array[i] # swapping 
    return array
# quick sort
def sortQuick (array, column):
    n = len(array)
    if n <= 1: # condition to return the array of size 1
        return array
    else:
        pivot = array[n // 2] # finding the pivot element
        rightArray = [x for x in array if x[column] > pivot[column]] #Values greater than pivot value
        leftArray = [x for x in array if x[column] < pivot[column]] #Values smaller than pivot value
        middleArray = [x for x in array if x[column] == pivot[column]] #Pivot value

        return sortQuick (leftArray,column) + middleArray + sortQuick(rightArray,column)

#merge sort
def mergeSort(array, column):
    if len(array) > 1: # condition
        mid = len(array) // 2  # finding the middle index
        left_half = array[:mid]  # items to the left of middle index
        right_half = array[mid:] # items to the right of middle index

       
        mergeSort(left_half, column) # recurrsion
        mergeSort(right_half, column) # recurrsion

        i = j = k = 0 # initializing variables

    
        while i < len(left_half) and j < len(right_half): # loop to compare and add values in the array for sorting
            if left_half[i][column] < right_half[j][column]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

       
        while i < len(left_half): # loops to add remaining values of left array in original array
            array[k] = left_half[i]
            i += 1
            k += 1

       
        while j < len(right_half): # loops to add remaining values of right array in original array
            array[k] = right_half[j]
            j += 1
            k += 1

    return array
# counting sort
def countingSort(array, column): 
 
    maxIndex = max(range(len(array)), key=lambda i: array[i][column]) # finding the index of max value
    maxValue = array[maxIndex][column] # finding the max value


    lengthArray = len(array) # length of array


    countingArray = [0] * (maxValue + 1)
    outputArray = [0] * lengthArray


    for value in array:
        index = value[column]
        countingArray[index] += 1

    for i in range(1, len(countingArray)):
        countingArray[i] += countingArray[i - 1]

 
    for value in array: 
        index = value[column]
        outputArray[countingArray[index] - 1] = value 
        countingArray[index] -= 1

   
    for i in range(lengthArray):
        array[i] = outputArray[i]

    return array

def radixC(arr, exp, column):
    n = len(arr)
    

    output = [0] * n

    count = [0] * 10


    for i in range(n):
        index = arr[i][column] // exp
        count[index % 10] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]


    i = n - 1
    while i >= 0:
        index = arr[i][column] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1


    for i in range(len(arr)):
        arr[i] = output[i]


def radixS(arr,column):

    max_val = max(row[column] for row in arr)

   
    exp = 1
    while max_val // exp > 0:
        radixC(arr, exp,  column)

        exp *= 10
    return arr


import math

def bucket_sort(arr, column):
    max_val = max(row[column] for row in arr)
    size = len(arr)
    
    buckets = [[] for _ in range(size)]
    
    for row in arr:
        index = math.floor(row[column] * size / (max_val + 1))
        buckets[index].append(row)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket, key=lambda x: x[column]))
    
    return sorted_arr



    


array = [
    [3, 'Alice', 85],
    [1, 'Bob', 90],
    [2, 'Charlie', 75],
    [4, 'David', 95],
    [5, 'Eve', 80]
]



  


