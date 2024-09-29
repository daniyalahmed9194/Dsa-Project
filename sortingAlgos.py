def bubbleSort (array, column):
    swapped = True
    i = 0
    n = len(array)
    while swapped:
        swapped = False
        for j in range (n-i-1):
            if array[j][column] > array[j+1][column]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        i = i + 1

    return array


def insertionSort (array, column):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j>=0 and array[j][column]>key[column]:
            array[j+1] = array [j]
            j = j - 1
        
        array [j+1] = key
    return array


def selectionSort (array,column):
    arrayLength = len(array)
    for i in range (0, arrayLength - 1):
        min = i
        for j in range (i+1,arrayLength):
            if array[j][column] < array[min][column]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array

def sortQuick (array, column):
    n = len(array)
    if n <= 1:
        return array
    else:
        pivot = array[n // 2]
        rightArray = [x for x in array if x[column] > pivot[column]]
        leftArray = [x for x in array if x[column] < pivot[column]]
        middleArray = [x for x in array if x[column] == pivot[column]]

        return sortQuick (leftArray,column) + middleArray + sortQuick(rightArray,column)

def mergeSort(array, column):
    if len(array) > 1:
        mid = len(array) // 2  
        left_half = array[:mid]  
        right_half = array[mid:]

       
        mergeSort(left_half, column)
        mergeSort(right_half, column)

        i = j = k = 0

    
        while i < len(left_half) and j < len(right_half):
            if left_half[i][column] < right_half[j][column]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

       
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

       
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array




array = [
    [3, 'Alice', 85],
    [1, 'Bob', 90],
    [2, 'Charlie', 75],
    [4, 'David', 95],
    [5, 'Eve', 80]
]

sortedArray = mergeSort(array, 1)

for row in sortedArray:
    print(row)


