def DFS(now, cnt):
    global result
    if cnt == 4:
        result = 1
        return
    visited[now] = 1
    for next in arr[now]:
        if not visited[next]:
            DFS(next, cnt + 1)
            visited[next] = 0

    

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = 0
for i in range(N):
    visited = [0] * N
    DFS(i, 0)
    if result:
        break
print(result)