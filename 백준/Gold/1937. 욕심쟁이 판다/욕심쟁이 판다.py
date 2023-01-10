import sys
sys.setrecursionlimit(250001)

def dfs(si, sj):
    if dp[si][sj]:
        return dp[si][sj]
    dp[si][sj] = 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < N:
            if forest[si][sj] < forest[ni][nj]:
                dp[si][sj] = max(dp[si][sj], dfs(ni, nj) + 1)
    return dp[si][sj]    

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)] # 그 칸에서 갈 수 있는 최대 이동거리
ans = 0

for i in range(N):
    for j in range(N):
        if ans < dfs(i, j):
            ans = dfs(i, j)

print(ans)