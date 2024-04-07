# Python program for implementation of Quicksort Sort, courtesy of geeksforgeeks.com
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
 
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
 
data = [9.09, 0.00, 22.22, 61.54, 23.53, 17.39, 27.78, 18.18, 25.93, 66.67, 62.50, 13.33, 25.00, 35.71, 42.86, 19.05, 53.33, 20.00, 23.53, 33.33, 27.27, 8.70, 15.38, 65.22, 80.00, 54.76, 68.42, 61.54, 11.11, 0.00, 166.67, 20.83, 50.00, 12.50, 82.35, 16.67, 54.84, 42.86, 62.50, 16.22, 45.00, 0.00, 9.52, 81.25, 33.33, 32.00, 37.50, 30.00, 50.00, 52.17, 136.67, 211.11, 42.31, 22.22, 90.00, 0.00, 42.86, 77.78, 53.85, 27.27, 57.14, 105.00, 40.00, 111.11, 19.05, 68.18, 85.71, 14.29, 42.86, 33.33, 31.58, 33.33, 16.00, 80.00, 47.37, 41.18, 0.00, 58.82, 38.10, 20.00, 129.63, 0.00, 57.14, 109.52, 13.33, 77.78, 46.15, 123.08, 87.50, 25.00, 25.00, 26.67, 52.00, 20.00, 21.05, 24.00, 0.00, 77.27, 33.33, 14.29, 60.00, 29.63, 37.50, 55.56, 60.00, 15.38, 0.00, 39.13, 78.57, 45.45, 35.71, 60.71, 85.71, 40.00, 138.89, 190.91, 57.14, 34.48, 83.33, 10.00, 50.00, 100.00, 59.09, 100.00, 40.74, 50.00, 80.00, 26.67, 29.63, 64.10, 76.67, 11.76, 47.06, 47.37, 46.43, 0.00, 32.43, 17.39, 58.33, 37.50, 29.63, 61.54, 32.35, 28.00, 33.33, 57.89, 29.17, 58.33, 92.00, 21.74, 75.00, 55.56, 26.09, 116.67, 40.00, 65.62, 72.00, 80.00, 13.33, 56.25, 91.30, 42.86, 117.65, 33.33, 60.71, 33.33, 44.00, 52.50, 45.83, 39.02, 252.63, 21.05, 103.57, 24.00, 22.86, 44.00, 70.59, 35.00, 38.89, 80.77, 60.87, 37.50, 35.29, 60.00, 38.71, 44.44, 56.67, 56.25, 72.22, 47.62, 32.00, 62.86, 33.33, 80.00, 38.30, 39.02, 68.42, 60.87, 36.36, 31.43]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)