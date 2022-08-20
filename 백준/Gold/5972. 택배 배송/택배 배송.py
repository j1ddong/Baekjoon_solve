from heapq import heappop, heappush

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
    arr[b].append((c, a))

check = [50000001] * (N + 1)
check[0] = 0
q = []
heappush(q, (0, 1))
while q:
    c, now = heappop(q)
    for nc, next in arr[now]:
        cost = c + nc
        if check[next] > cost:
            check[next] = cost
            heappush(q, (cost, next))
        
print(check[N])