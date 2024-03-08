#Merge Sort 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
  
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
  
  
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
  
    return merge(left_half, right_half)

#define the merge function 
def merge(left, right):
    result = []
    left_index = right_index = 0
  
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
  
    result.extend(left[left_index:])
    result.extend(right[right_index:])
  
    return result
#test the merge sort
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = mergeSort(arr)
print("Sorted array is: ", sorted_arr) #result: " Sorted array is:  [5, 6, 7, 11, 12, 13] "
