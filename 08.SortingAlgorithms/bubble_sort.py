arr = list(range(10, 0, -1))

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

print("Before sorting: ", arr)
bubbleSort(arr)
print("After sorting: ", arr)
