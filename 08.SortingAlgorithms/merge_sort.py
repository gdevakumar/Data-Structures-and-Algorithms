def merge(list1, list2):
    sorted_arr = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_arr.append(list1[i])
            i += 1
        else:
            sorted_arr.append(list2[j])
            j += 1
    while i < len(list1):
        sorted_arr.append(list1[i])
        i += 1
    while j < len(list2):
        sorted_arr.append(list2[j])
        j += 1
    return sorted_arr

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid_index = len(arr)//2
    left = mergeSort(arr[:mid_index])
    right = mergeSort(arr[mid_index:])

    return merge(left, right)


original_list = [3,1,4,2]

sorted_list = mergeSort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)
