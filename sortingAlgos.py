import math
from Utilityfunc import clean_numeric_value

# bubble sort
def bubbleSort (array, column):
    swapped = True # flag
    i = 0
    n = len(array) # length of array
    while swapped: # outer loop will break if array is already sorted
        swapped = False
        for j in range (n-i-1): # inner loop
            if clean_numeric_value(array[j][column],column)> clean_numeric_value(array[j+1][column],column):  # sorting condition
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
        while j>=0 and clean_numeric_value(array[j][column],column)>clean_numeric_value(key[column],column): # comparing values
            array[j+1] = array [j]
            j = j - 1
        
        array [j+1] = key
    return array

# selection sort
def selectionSort(array, column):
    arrayLength = len(array)
    for i in range(arrayLength - 1):
        min_index = i  # index of minimum value in the array
        for j in range(i + 1, arrayLength):
            # Clean both the values before comparison
            if clean_numeric_value(array[j][column], column) < clean_numeric_value(array[min_index][column], column):
                min_index = j
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]
    return array
# quick sort
def sortQuick (array, column):
    n = len(array)
    if n <= 1: # condition to return the array of size 1
        return array
    else:
        pivot = array[n // 2] # finding the pivot element
        rightArray = [x for x in array if clean_numeric_value(x[column],column) > clean_numeric_value(pivot[column],column)] #Values greater than pivot value
        leftArray = [x for x in array if clean_numeric_value(x[column],column) < clean_numeric_value(pivot[column],column)] #Values smaller than pivot value
        middleArray = [x for x in array if clean_numeric_value(x[column],column) == clean_numeric_value(pivot[column],column)] #Pivot value

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
            if clean_numeric_value(left_half[i][column],column) < clean_numeric_value(right_half[j][column],column):
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
    # Get the minimum and maximum values after cleaning
    cleaned_values = [clean_numeric_value(item[column], column) for item in array]
    # min_value = min(cleaned_values)
    max_value = max(cleaned_values)
    
    length_array = len(array)

    # Adjust the range to account for negative values
    range_of_values = int(max_value + 1)  # Total range of values

    # Create counting array and output array
    counting_array = [0] * range_of_values
    output_array = [0] * length_array

    # Count occurrences of each cleaned value
    for value in array:
        index = int(clean_numeric_value(value[column], column))  # Adjust index by subtracting min_value
        counting_array[index] += 1

    # Modify counting array to hold the position of values
    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i - 1]

    # Build the output array
    for value in reversed(array):  # To maintain stability, iterate in reverse order
        index = int(clean_numeric_value(value[column], column))
        output_array[counting_array[index] - 1] = value
        counting_array[index] -= 1

    # Copy the output array to the original array
    for i in range(length_array):
        array[i] = output_array[i]

    return array


def radixC(arr, exp, column):
    n = len(arr)
    output = [0] * n

    # Use a counting array large enough to cover all possible digit values
    count = [0] * 20  # Adjust size if you expect larger values

    # Store the count of occurrences of each digit
    for i in range(n):
        index = int(clean_numeric_value(arr[i][column], column)) // exp
        count[index % 10 + 10] += 1  # Shift by +10 to handle negative values

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array using the count array
    for i in range(n - 1, -1, -1):
        index = int(clean_numeric_value(arr[i][column], column)) // exp
        output[count[index % 10 + 10] - 1] = arr[i]
        count[index % 10 + 10] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]


def radixS(arr, column):
    # Get the maximum value to figure out the number of digits
    max_value = int(max(clean_numeric_value(item[column], column) for item in arr))

    # Perform counting sort for every digit
    exp = 1
    while max_value // exp > 0:
        radixC(arr, exp, column)
        exp *= 10
    
    return arr



def bucket_sort(arr, column):
    # Get the minimum and maximum values after cleaning
    cleaned_values = [clean_numeric_value(row[column], column) for row in arr]
    min_val = min(cleaned_values)
    max_val = max(cleaned_values)
    size = len(arr)
    
    # Adjust range of the buckets
    range_of_values = max_val - min_val  # Total range of values
    
    # Create buckets
    buckets = [[] for _ in range(size)]
    
    # Place array elements into their respective buckets
    for row in arr:
        normalized_value = (clean_numeric_value(row[column], column) - min_val) / (range_of_values + 1)
        index = math.floor(normalized_value * size)
        buckets[index].append(row)
    
    # Sort individual buckets and concatenate them
    sorted_arr = []
    for bucket in buckets:
<<<<<<<<< Temporary merge branch 1
        bucket = mergeSort(bucket,column)
    for bucket in buckets:
        sorted_arr.extend(bucket)
=========
        sorted_arr.extend(sorted(bucket, key=lambda x: clean_numeric_value(x[column], column)))
>>>>>>>>> Temporary merge branch 2
    
    return sorted_arr




   



