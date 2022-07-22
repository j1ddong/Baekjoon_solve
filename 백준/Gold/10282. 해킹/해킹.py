from heapq import heappop, heappush

def dijkstra(start):
    q = []
    visited = [90000000] * (n + 1)
    heappush(q, (0, start))
    visited[start] = 0
    while q:
        # print(f'q: {q}')
        ctime, cnode = heappop(q)
        # print(f'cnode: {cnode}')
        for ntime, nnode in graph[cnode]:
            if visited[nnode] > visited[cnode] + ntime:
                visited[nnode] = visited[cnode] + ntime
                heappush(q, (ntime, nnode))
    cnt = time = 0
    for i in range(n + 1):
        if visited[i] < 90000000:
            cnt += 1
            time = max(time, visited[i])
    print(cnt, time)


TC = int(input())
for _ in range(TC):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, t = map(int, input().split())
        graph[b].append((t, a))
    dijkstra(c)