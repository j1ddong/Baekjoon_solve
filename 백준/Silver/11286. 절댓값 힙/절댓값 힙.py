import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = []
for _ in range(N):
    X = int(input())
    if X > 0:
        heappush(arr, (X, X))
    elif X < 0:
        heappush(arr, (-X, X))
    else:
        if len(arr):
            print(heappop(arr)[1])
        else:
            print(0)