def sorted_array(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True


a = [2, 3, 4, 5, 6, 7, 8, 9]

print(sorted_array(a))
