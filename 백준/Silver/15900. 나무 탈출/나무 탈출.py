import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

def dfs(node, cnt):
    global ans
    visited[node] = 1
    if node != 1 and len(arr[node]) == 1:
        ans += cnt
    for elem in arr[node]:
        if not visited[elem]:
            dfs(elem, cnt + 1)


N = int(input())
arr = [[] for _ in range(N + 1)]
ans = 0
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N + 1)
dfs(1, 0)
if ans % 2:
    print('Yes')
else:
    print('No')

