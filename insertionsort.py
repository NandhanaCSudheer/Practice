arr = list(map(int, input("Enter the elements: ").split()))
n = len(arr)
# Traverse from the second element
for i in range(1, n):
    key = arr[i]      # Element to be inserted
    j = i - 1         # Last index of the sorted part
    # Shift elements greater than key to one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    # Insert the key at its correct position
    arr[j + 1] = key
print("Sorted array:", arr)