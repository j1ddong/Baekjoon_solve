import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(start):
    global visited
    visited[start] = 1
    if len(tree[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in tree[start]:
            if not visited[i]:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1]) 
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0],dp[1][1]))