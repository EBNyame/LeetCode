arr = [2, 3, 1, 20, 15]
k = 4
def smallest(arr, k):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] < arr[j -1]:
                arr[j], arr[j -1] = arr[j -1], arr[j]

    return arr[k-1]

print(smallest(arr, k))