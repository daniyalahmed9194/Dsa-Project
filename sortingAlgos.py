import math
def clean_numeric_value(value, column):
    # Remove 'Rs.' and commas, and convert the string to a float
    if(column==1):
        try:
            # Strip the currency symbol and commas, then convert to float
            cleaned_value = float(value.replace('Rs.', '').replace(',', '').strip())
        except ValueError:
            # Handle the case where the value cannot be converted (optional)
            cleaned_value = 0.0  # Default value for invalid entries
        return cleaned_value
    elif (column==2):
        try:
            cleaned_value = int(value*10)
        except ValueError:
            cleaned_value = 0
        return cleaned_value
    elif (column==3):
        try:
            if (value=='No discount'):
                cleaned_value = 0
            else:
                cleaned_value = float(value.replace('%', '').replace('Off', '').strip())
        except ValueError:
            cleaned_value = 0.0  # Default value for invalid entries
        return cleaned_value
    elif (column==5):
        cleaned_value = value.replace('sold', '').strip()
    
        try:
            # Check if it ends with 'K' for thousands
            if cleaned_value.endswith('K'):
                # Convert to float and multiply by 1000
                cleaned_value = float(cleaned_value[:-1]) * 1000  
            else:
                # Convert directly to float
                cleaned_value = float(cleaned_value)
        except ValueError:
            # Handle cases where conversion fails
            cleaned_value = 0.0
        cleaned_value = math.floor(cleaned_value)
        return cleaned_value
    else:
        return value
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
    # Get the maximum value after cleaning
    max_value = max(clean_numeric_value(item[column], column) for item in array)
    length_array = len(array)

    # Create counting array and output array
    counting_array = [0] * (int(max_value) + 1)
    output_array = [None] * length_array

    # Count occurrences of each cleaned value
    for value in array:
        index = int(clean_numeric_value(value[column], column))
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
    max_val = max(clean_numeric_value(row[column],column) for row in arr)
    size = len(arr)
    
    buckets = [[] for _ in range(size)]
    
    for row in arr:
        index = math.floor(clean_numeric_value(row[column],column) * size / (max_val + 1))
        buckets[index].append(row)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket, key=lambda x: x[column]))
    
    return sorted_arr



   



