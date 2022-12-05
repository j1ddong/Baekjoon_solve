import sys
input = sys.stdin.readline

N = int(input())
         
# dp [현재 자릿수 7자리 len => 3][현재 사용한 숫자 3][현재까지 사용한 숫자 1, 2, 3]
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]
ans = 0

for i in range(1, 10):
    dp[1][i][1<<i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1 << 10):
            if j != 9:
                dp[i + 1][j + 1][k | 1<<(j + 1)] += dp[i][j][k]
            if j != 0:
                dp[i + 1][j - 1][k | 1<<(j - 1)] += dp[i][j][k]

for i in range(10):
    ans+= dp[N][i][(1<<10) - 1]

print(ans%1000000000)