import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    sc, ec, cost = map(int, input().split())
    bus[sc].append([ec, cost])
s, e = list(map(int, input().split()))


arr = [1000000000 for _ in range(N + 1)]
arr[s] = 0

def dijkstra(s):
    q = []
    heappush(q, [0, s])
    while q:
        cost, now = heappop(q)
        if arr[now] < cost:
            continue
        for ec, c in bus[now]:
            if arr[ec] > cost + c:
                arr[ec] = cost + c
                heappush(q, [cost + c, ec])



dijkstra(s)
print(arr[e])
