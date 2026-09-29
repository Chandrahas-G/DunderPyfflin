# WIth Fucntion
def diff():
    a = [3, 4, 1, 6, 9, 2]
    max_diff = 0

    for i in range(len(a) - 1):
        abs_diff = abs(a[i + 1] - a[i])

        if max_diff < abs_diff:
            max_diff = abs_diff

    print(max_diff)

diff()

# Without funciton
a = [3, 4, 1, 6, 9, 2]
max_diff = 0

for i in range(len(a) - 1):
    abs_diff = abs(a[i + 1] - a[i])

    if max_diff < abs_diff:
         max_diff = abs_diff

print(max_diff)
