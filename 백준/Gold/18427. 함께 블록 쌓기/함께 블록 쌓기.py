N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
dp = [[1] + [0] * H for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, H + 1):
        temp = 0
        for w in blocks[i - 1]:
            if j - w >= 0:
                temp += dp[i - 1][j - w]
        dp[i][j] += dp[i - 1][j] + temp

print(dp[-1][-1] % 10_007)