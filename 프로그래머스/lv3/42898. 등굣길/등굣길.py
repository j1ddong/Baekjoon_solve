def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] 
    memo = [[0] * (m + 1) for _ in range(n + 1)]
    memo[1][1] = 1  # 집의 위치
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if [i, j] in puddles:
                memo[i][j] = 0
            else:
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[n][m] % 1000000007