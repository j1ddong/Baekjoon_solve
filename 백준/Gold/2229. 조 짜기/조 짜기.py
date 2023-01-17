N = int(input())
arr = list(map(int, input().split()))

# i명까지 짰을 때 최댓값
dp = [0] * N
for i in range(1, N):
    dp[i] = dp[i - 1]
    for j in range(i - 1, -1, -1):
        temp = arr[j:i + 1]
        jungdo = abs(max(temp) - min(temp))
        if j == 0:
            dp[i] = max(dp[i], jungdo)
        else:
            dp[i] = max(dp[i], jungdo + dp[j - 1])

print(dp[-1])