def is_black(length, ci, cj):
    center = length // N
    if length == 1:
        return 0
    if center * (N - K) // 2 <= ci < center * (N + K) // 2 and center * (N - K) // 2 <= cj < center * (N + K) // 2:
        return 1
    ci %= center
    cj %= center
    return is_black(center, ci, cj)


T, N, K, R1, R2, C1, C2 = map(int, input().split())
length = N ** T
for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        print(is_black(length, i, j), end='')
    print()
