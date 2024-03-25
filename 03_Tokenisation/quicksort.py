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
 
 
data = [8.70, 0.00, 21.43, 47.06, 23.53, 16.00, 23.81, 16.67, 22.58, 48.48, 44.44, 12.50, 22.22, 29.41, 35.29, 17.39, 42.11, 18.18, 21.05, 28.57, 23.08, 8.33, 14.29, 45.45, 57.14, 41.82, 48.15, 47.06, 10.53, 0.00, 71.43, 18.52, 39.13, 11.76, 51.85, 15.38, 41.46, 34.62, 45.45, 15.00, 36.00, 0.00, 9.09, 52.00, 28.57, 27.59, 31.03, 25.71, 41.67, 40.00, 67.21, 79.17, 34.38, 20.00, 54.55, 0.00, 35.29, 58.33, 38.89, 24.00, 40.00, 61.76, 33.33, 68.97, 17.39, 50.00, 60.00, 13.33, 34.88, 28.57, 27.27, 28.57, 14.81, 52.17, 37.50, 33.33, 0.00, 45.45, 32.00, 18.18, 66.04, 0.00, 42.11, 60.53, 12.50, 53.85, 35.29, 65.31, 56.00, 22.22, 22.22, 23.53, 38.24, 18.18, 19.05, 22.22, 0.00, 53.12, 28.57, 13.33, 45.00, 25.81, 31.58, 41.67, 42.86, 14.29, 0.00, 32.14, 55.00, 35.71, 29.41, 43.59, 54.55, 33.33, 67.57, 77.78, 44.44, 28.57, 53.57, 9.52, 38.89, 60.87, 43.33, 62.50, 33.33, 36.17, 53.33, 23.53, 27.59, 44.64, 53.49, 11.11, 36.36, 36.00, 37.14, 0.00, 28.57, 16.00, 43.75, 31.58, 27.59, 47.06, 26.83, 24.14, 28.00, 42.31, 25.00, 43.75, 52.27, 20.00, 53.57, 41.67, 23.08, 60.00, 33.33, 48.84, 51.43, 54.55, 12.50, 42.86, 55.26, 33.33, 60.61, 28.57, 43.59, 28.00, 36.67, 39.62, 35.48, 30.19, 81.36, 19.05, 60.42, 21.43, 20.51, 34.38, 52.17, 29.17, 31.82, 52.50, 45.16, 31.58, 30.00, 42.86, 30.77, 38.10, 40.48, 40.91, 46.43, 38.46, 27.59, 46.81, 28.00, 53.33, 31.03, 32.00, 48.15, 45.16, 30.30, 26.83]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)