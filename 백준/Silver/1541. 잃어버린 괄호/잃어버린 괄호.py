numbers = input().split('-')
ans = 0

for i in range(len(numbers)):
    temp = 0
    for number in numbers[i].split('+'):
        temp += int(number)
    if not i:
        ans = temp
    else:
        ans -= temp
print(ans)
