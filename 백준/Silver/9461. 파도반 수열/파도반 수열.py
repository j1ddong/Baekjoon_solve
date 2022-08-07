T = int(input())


memo = [0] * 101
memo[1] = memo[2] = memo[3] = 1


for _ in range(T):
    N = int(input())
    if memo[N]:
        print(memo[N])
    else:
        for i in range(4, N + 1):
            memo[i] = memo[i - 2] + memo[i - 3]
        print(memo[N])
