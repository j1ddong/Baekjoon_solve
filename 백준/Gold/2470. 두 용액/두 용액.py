import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 3000000000
left, right = 0, len(arr) - 1
al = ar = 0


while left < right:
    temp = arr[right] + arr[left]
    if abs(temp) < ans:
        ans = abs(temp)
        al, ar = arr[left], arr[right]
    if temp > 0:
        right -= 1
    else:
        left += 1


print(al, ar)