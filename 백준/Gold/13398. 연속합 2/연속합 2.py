import sys

N = int(input())
arr = list(map(int, input().split()))
# 제거 무 최대합, 제거 유 최대합
dp = [[0] * N for _ in range(2)]
dp[0][0] = arr[0]

if N > 1:
    max_number = -1e9
    for i in range(1, N):
        dp[0][i] = max(arr[i], dp[0][i - 1] + arr[i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

        max_number = max(max_number, dp[0][i], dp[1][i])
    print(max_number)
else:
    print(dp[0][0])