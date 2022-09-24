import heapq

def solution(n, edges):
    nodes = [[] for _ in range(n + 1)]
    for a, b in edges:
        nodes[a].append(b)
        nodes[b].append(a)
    q = [(0, 1)]
    visited = [-1] * (n + 1)
    visited[1] = 0
    while q:
        cnt, now = heapq.heappop(q)
        for next in nodes[now]:
            if visited[next] == -1:
                visited[next] = cnt + 1
                heapq.heappush(q, (cnt + 1, next))
    max_num = max(visited)
    return visited.count(max_num)