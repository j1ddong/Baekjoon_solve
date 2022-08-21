from heapq import heappop, heappush

n, limit, r = map(int, input().split())
items = list(map(int, input().split()))
roads = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, w = map(int, input().split())
    roads[a].append((w, b))
    roads[b].append((w, a))

ans = 0

def dijkstra(start):
    check[start] = 0
    q = [(0, start)]
    while q:
        cw, current = heappop(q)
        for dw, next in roads[current]:
            if check[next] > cw + dw:
                check[next] = cw + dw
                heappush(q, (cw + dw, next)) 

for i in range(1, n + 1):
    check = [30001] * (n + 1)
    cnt = items[i - 1]
    dijkstra(i)
    for j in range(1, n + 1):
        if check[j] and check[j] <= limit:
            cnt += items[j - 1]
    ans = max(ans, cnt)
    

print(ans)