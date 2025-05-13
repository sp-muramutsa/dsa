def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i -1
        key = arr[i]

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(arr)
        
        print("\n")
        arr[j+1] = key

    return arr
arr = [23, 1, 10, 5, 2]
sorted_arr = insertion_sort(arr)
print(sorted_arr)