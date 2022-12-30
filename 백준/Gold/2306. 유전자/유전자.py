def sol(start, end):
    if start >= end:
        return 0

    if dp[start][end] != -1:
        return dp[start][end]

    max_number = 0
    for cut in range(start, end):
        max_number = max(max_number, sol(start, cut) + sol(cut + 1, end))

    if (DNA[start] == 'a' and DNA[end] == 't') or (DNA[start] == 'g' and DNA[end] == 'c'):
        max_number = max(max_number, sol(start + 1, end - 1) + 2)
    dp[start][end] = max_number
    return dp[start][end]

    
DNA = input()
N = len(DNA)
dp = [[-1] * N for _ in range(N)]

print(sol(0, N - 1))