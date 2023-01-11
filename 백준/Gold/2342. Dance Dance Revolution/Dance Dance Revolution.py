orders = list(map(int, input().split()))
INF = 1e9
dp = [[[0] * 5 for _ in range(5)] for _ in range(len(orders))]
dp[0][0][0] = 1

for i in range(1, len(orders)):
    for l in range(5):
        for r in range(5):
            if dp[i - 1][l][r]:
                target = orders[i - 1]
                if l == 0:
                    left = dp[i - 1][l][r] + 2
                else:
                    force = 0
                    if abs(target - l) == 2:
                        force = 4
                    elif target == l:
                        force = 1
                    else:
                        force = 3
                    left = dp[i - 1][l][r] + force

                if r == 0:
                    right = dp[i - 1][l][r] + 2
                else:
                    force = 0
                    if abs(target - r) == 2:
                        force = 4
                    elif target == r:
                        force = 1
                    else:
                        force = 3
                    right = dp[i - 1][l][r] + force

                if dp[i][target][r] == 0:
                    dp[i][target][r] = left
                else:
                    dp[i][target][r] = min(dp[i][target][r], left)

                if dp[i][l][target] == 0:
                    dp[i][l][target]= right
                else:
                    dp[i][l][target] = min(dp[i][l][target], right)

power = INF
for l in range(5):
    for r in range(5):
        now = dp[-1][l][r]
        if now and power > now:
            power = now
print(power - 1)