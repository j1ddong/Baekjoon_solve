N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
left, right = 0, len(arr) - 1
cnt = 0

while left < right:
    temp = arr[left] + arr[right]
    if temp == X:
        cnt += 1
    if temp > X:
        right -= 1
    else:
        left += 1

print(cnt)