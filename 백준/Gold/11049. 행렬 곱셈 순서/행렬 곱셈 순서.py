import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for size in range(1, N):
    for start in range(N - size):
        end = start + size
        dp[start][end] = 1e9
        for i in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][i] + dp[i + 1][end] + lst[start][0] * lst[i][1] * lst[end][1])

print(dp[0][N - 1])
