# Using for loop
text = "Jai Mahishmathi"

for i in range(len(text) - 1, -1, -1):  # range(start, stop, step)
    print(text[i], end="")

# Using Slice
text = "Jai Mahishmathi"
print(text[::-1])

# Using another String
text = "Jai Mahishmathi"
reverse = ""

for i in range(len(text) - 1, -1, -1):
    c = text[i]
    reverse = reverse + c

print(reverse)
