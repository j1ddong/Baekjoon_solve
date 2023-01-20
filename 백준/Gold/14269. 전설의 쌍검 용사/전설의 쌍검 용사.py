N = int(input())
arr = []
dp = [0] * 1000001
cnt = 0

for _ in range(N):
    A, B, C = map(int, input().split())
    arr.append([A, B, C])
    dp[A] = 1

arr.sort(key=lambda x: (x[1], x[2]))
et = 0

for i in range(N):
    t_left, t_start, t_end = arr[i]
    for elem in range(t_start, t_end + 1):
        if t_left != elem and dp[elem]:
            break
    else:
        if arr[i][1] >= et:
            left, st, et = arr[i]
            cnt += 1

for i in range(1000001):
    if dp[i]:
        cnt += 1

print(cnt)