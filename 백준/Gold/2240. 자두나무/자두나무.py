T, W = map(int, input().split())
dp = [[[0] * (T + 1) for _ in range(2)] for _ in range(W + 1)]
arr = [0] + [int(input()) for _ in range(T)]

dp = [[0] * (W + 1) for _ in range(T + 1)]

for t in range(T + 1):
    if arr[t] == 1:
        dp[t][0] = dp[t - 1][0] + 1
    elif arr[t] == 2:
        dp[t][0] = dp[t - 1][0]

    for w in range(1, W + 1):
        if (arr[t] == 2) and (w % 2 == 1):
            dp[t][w] = max(dp[t - 1][w - 1], dp[t - 1][w]) + 1
        elif (arr[t] == 1 and w % 2 == 0):
            dp[t][w] = max(dp[t - 1][w - 1], dp[t - 1][w]) + 1
        else:
            dp[t][w] = max(dp[t - 1][w - 1], dp[t - 1][w])

print(max(dp[T]))