# as Sorted() retunrs lists already
str3 = "Mary"
str4 = "Army"

if sorted(str3.lower()) == sorted(str4.lower()):
    print("Anagram")
else:
    print("Not an Anagram")
  
# With loops and If conditions
str3 = "Mary"
str4 = "Army"

if len(str3) == len(str4):
    str1 = sorted(str3.lower())
    str2 = sorted(str4.lower())

    boolean = True
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            boolean = False
            break

    print("Anagram") if boolean else print("Not an Anagram")

else:
    print("Not an Anagram")
