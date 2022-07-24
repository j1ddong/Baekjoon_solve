import sys
input = sys.stdin.readline

from heapq import heappop, heappush


N = int(input())
arr = []
for _ in range(N):
    X = -int(input())
    if X == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heappop(arr))
    else:
        heappush(arr, X)