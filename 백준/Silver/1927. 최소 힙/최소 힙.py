import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
arr = []
for _ in range(N):
    X = int(input())
    if X == 0:
        if len(arr):
            print(heappop(arr))
        else:
            print(0)
    else:
        heappush(arr, X)