import sys
input = sys.stdin.readline

def tsp(now, visited):
    if dp[now][visited] != 0:
        return dp[now][visited]

    if visited == (1 << N) - 1:
        return costs[now][0] if costs[now][0] else INF
    
    dp[now][visited] = INF

    for i in range(1, N):
        if not costs[now][i]:
            continue
        bit = 1 << i
        if (visited & bit) > 0:
            continue
        dp[now][visited] = min(dp[now][visited], tsp(i, visited | bit) + costs[now][i])
    return dp[now][visited]



N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
INF = 16000001
dp = [[0] * (1 << N) for _ in range(N)]
print(tsp(0, 1))