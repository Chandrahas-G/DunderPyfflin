# With Functions
print(max(data))
print(min(data))

# Minimum
data = [3,5,1,8,2,9]
min = data[0]

for i in range(len(data)):
  if min > data[i]:
    min = data[i]

print(min)

# Maximum 
data = sorted(data)
print(data[len(data)-1])
