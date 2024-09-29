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


array = [
    [3, 'Alice', 85],
    [1, 'Bob', 90],
    [2, 'Charlie', 75],
    [4, 'David', 95],
    [5, 'Eve', 80]
]


