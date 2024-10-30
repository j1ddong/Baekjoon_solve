import math

num = input()
numDir = {}
result = 0

# dir init
for i in range(0, 9):
    numDir[i] = 0

for n in num:
    if n == '9':
        numDir[6] += 1
    else:
        numDir[int(n)] += 1

for i in range(0, 9):
    if i == 6:        
        numDir[i] = math.ceil(numDir[i] / 2)
    
    result = max(result, numDir[i])

print(result)