def bucket_sort(arr):
    n = len(arr)

    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

        for bucket in buckets:
            bucket.sort()

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1


arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))
