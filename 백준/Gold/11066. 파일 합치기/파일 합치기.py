import sys

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    sub_sum = [0] * (K + 1)
    for idx, file in enumerate(files):
        sub_sum[idx] = file + sub_sum[idx - 1]

    dp = [[0] * K for _ in range(K)]

    for size in range(1, K):
        for start in range(K - 1):
            end = start + size

            if end >= K:
                continue

            result = 50000000001
            for cut in range(start, end):
                result = min(result, dp[start][cut] + dp[cut + 1][end] + sub_sum[end] - sub_sum[start - 1])
            dp[start][end] = result
    print(dp[0][-1])