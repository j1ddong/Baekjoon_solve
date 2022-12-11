import sys

N = input()
length = len(N) + 1
dp = [0] * length

if N[0] == '0':
    print(0)
else:
    dp[0] = dp[1] = 1
    N = '0' + N
    for i in range(2, length):
        if int(N[i]):
            dp[i] += dp[i-1]
        if 9 < int(N[i-1] + N[i]) < 27:
            dp[i] += dp[i - 2]

    print(dp[-1] % 1000000)