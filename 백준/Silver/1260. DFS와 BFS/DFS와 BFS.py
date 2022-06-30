from collections import deque

def DFS(start):
    visitied = [0] * (N + 1)
    s = [start]
    while s:
        now = s.pop()
        if not visitied[now]:
            visitied[now] = 1
            print(now, end=' ')
        for i in arr[now]:
            if not visitied[i]:
                s.append(i)
    # print(f'DFS방문 표시{visitied}')


def BFS(start):
    visited = [0] * (N + 1)
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in arr[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1



N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(N + 1):
    arr[i].sort(reverse=True)
DFS(V)
print()
for i in range(N + 1):
    arr[i].sort()
BFS(V)