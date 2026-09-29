def sorted_list(a,n):
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False

    return True


a = [2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
print(sorted_list(a,n))
