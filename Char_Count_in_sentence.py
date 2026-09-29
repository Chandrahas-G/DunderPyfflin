str1 = "Jai Mahishmathi"
str1.lower()

char_count = {}

for i in range(len(str1)):
    c = str1[i]

    if c != ' ':
        if c in char_count:
            char_count[c] = char_count[c] + 1
        else:
            char_count[c] = 1

print(char_count)
