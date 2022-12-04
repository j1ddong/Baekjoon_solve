import sys

N, M = map(int, input().split())
memories  = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
column = sum(costs)
ans = 10001

# dp[i][j] i번째 앱까지 j 비용으로 얻을 수 있는 최대 메모리
dp = [[0] * (column + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, column + 1):
        if costs[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], memories[i] + dp[i - 1][j - costs[i]])
        
        if dp[i][j] >= M:
            ans = min(ans, j)

if M == 0:
    print(0)
else:
    print(ans) 