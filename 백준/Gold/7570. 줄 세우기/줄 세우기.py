N = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * (N + 1) for _ in range(2)]

for idx, elem in enumerate(arr):
    if dp[0][elem] == -1:
        dp[0][elem], dp[1][elem] = idx, 1
    if dp[0][elem - 1] != -1 and dp[0][elem - 1] < idx:
        dp[1][elem] = dp[1][elem - 1] + 1
    
print(N - max(dp[1]))