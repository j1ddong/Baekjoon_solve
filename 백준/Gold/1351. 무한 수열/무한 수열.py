def sol(curr):
    if dp.get(curr):
        return dp[curr]
    dp[curr] = sol(curr // P) + sol(curr // Q)
    return dp[curr]

N, P, Q = map(int, input().split())
dp = {0: 1}
sol(N)
print(dp[N])