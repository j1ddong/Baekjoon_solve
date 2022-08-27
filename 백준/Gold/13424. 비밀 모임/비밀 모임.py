from collections import deque


def dijkstra(order, start):
    q = deque([(0, start)])
    ans[start][order] = 0
    while q:
        w, now = q.popleft()
        for next, nw in arr[now]:
            if ans[next][order] > w + nw:
                ans[next][order] = w + nw
                q.append((nw + w, next))
    

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
        arr[b].append((a, c))
    K = int(input())
    ans = [[1000000] * K  for _ in range(N + 1)]
    locations = list(map(int, input().split()))
    
    for i in range(K):
        dijkstra(i, locations[i])
    min_number = 10000000000000
    result = -1
    for i in range(1, N + 1):
        if min_number > sum(ans[i]): 
            min_number = sum(ans[i])
            result = i
    print(result)