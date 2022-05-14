import heapq, sys


V, E = map(int, input().split())
result = 0
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def MST(s):
    global result
    cnt = 0
    connected = [0] * (V + 1)
    next = [(0, s)]
    while cnt != V:
        w, now = heapq.heappop(next)
        if not connected[now]:  # 아직 MST에 연결되어 있지 않으면
            result += w 
            connected[now] = 1
            for elem in graph[now]:
                heapq.heappush(next, elem)
            cnt += 1


MST(1)
print(result)