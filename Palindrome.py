# Python Fucntion to reverse string
n = "12345654321"

if str(n) == str(n)[::-1]:
  print("Palindrome")
else:
  print("Not Palindrome")

# with Loop
def palindrome_check(n):
    rev = 0

    while n > 0:
        temp = n % 10
        rev = (rev * 10) + temp
        n = n // 10

    return rev

n = 1234564321
rev = palindrome_check(n)

if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")
