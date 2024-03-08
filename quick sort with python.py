#Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lower = [x for x in arr[1:] if x <= pivot]
        higher = [x for x in arr[1:] if x > pivot]
        return quick_sort(lower) + [pivot] + quick_sort(higher)

#test the function
arr = [5, 2, 9, 1, 7, 6, 3, 8, 4]
sorted_arr = quick_sort(arr)
print(sorted_arr) # result of print[1, 2, 3, 4, 5, 6, 7, 8, 9]