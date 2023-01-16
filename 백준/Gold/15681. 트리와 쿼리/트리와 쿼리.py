import sys

input = sys.stdin.readline
sys.setrecursionlimit(100001)

def find_nodes(curr):
    visited[curr] = 1
    if dp[curr]:
        return dp[curr]
    for next in graph[curr]:
        if not visited[next]:
            dp[curr] += find_nodes(next)
    dp[curr] += 1
    return dp[curr]
    

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
dp = [0] * (N + 1)
find_nodes(R)

for _ in range(Q):
    U = int(input())
    print(dp[U])