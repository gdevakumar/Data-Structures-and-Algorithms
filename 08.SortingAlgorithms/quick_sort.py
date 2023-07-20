# In this implementation, we are using 1st element in the array as pivot

def partition(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
    arr[pivot_index], arr[swap_index] = arr[swap_index],  arr[pivot_index]
    return swap_index

def quickSort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quickSort(arr, left, pivot_index-1)
        quickSort(arr, pivot_index+1, right)
    return arr


original_list = [4,6,1,7,3,2,5]

print('Before Sorting:', original_list)

quickSort(original_list, 0, len(original_list)-1)

print('\nAfter Sorting:', original_list)