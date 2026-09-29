arr = [2, 5, 1, 3, 7, 6]

# range(start, stop, step)    
for i in range(len(arr) - 1, 0, -1):  # How many rounds?
    for j in range(i):                # Which elements to compare?
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
