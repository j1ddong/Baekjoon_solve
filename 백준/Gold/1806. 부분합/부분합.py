import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

startidx = endidx = subsum = 0
ans = 100001

while True:
    if subsum >= S:
        ans = min(ans, endidx - startidx)
        subsum -= arr[startidx]
        startidx += 1
    elif endidx == N:
        break
    else:
        subsum += arr[endidx]
        endidx += 1
if sum(arr) < S:
    print(0)
else:
    print(ans)