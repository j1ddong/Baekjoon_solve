import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)
for i in range(N):
    day, money = schedule[i]
    next = day + i
    dp[i] = max(dp[i], dp[i - 1])
    if next <= N:
        dp[next] = max(dp[next], dp[i] + money)

print(max(dp))