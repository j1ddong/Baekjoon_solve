import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = arr[0] # 1개는 반드시 선택해야 한다.

    if N > 1:
        ans = -1e9
        for i in range(1, N):
            dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
            dp[1][i] = max(dp[0][i - 1], dp[1][i-1] + arr[i])
            ans = max(ans, dp[0][i], dp[1][i])
        print(ans)
    else: # N이 1인 경우는 반드시 선택을 해야하므로 dp[0][0] 출력
        print(dp[0][0])