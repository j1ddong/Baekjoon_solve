import sys
from queue import PriorityQueue

N = int(input())
present = PriorityQueue()
for i in range(N):
    a = list(input().split())
    if len(a) > 1:
        for i in a[1:]:
            i = int(i)
            present.put((-i, i))
    else:
        if present.empty():
            print(-1)
        else:
            gift = present.get()
            print(gift[1])