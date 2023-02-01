N = int(input())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, len(arr) - 1
ans = 2_000_000_000
left, rigth = 0, 0

while start < end:
    curr = arr[start] + arr[end]
    if abs(curr) < ans:
        ans = abs(curr)
        left, right = arr[start], arr[end]
    if curr == 0:
        left, right = arr[start], arr[end]
        break
    elif curr > 0:
        end -= 1
    elif curr < 0:
        start += 1

print(left, right)