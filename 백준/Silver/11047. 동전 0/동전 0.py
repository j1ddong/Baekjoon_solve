N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 0

while K:
    for i in range(len(arr) -1, -1, -1):
        if arr[i] <= K:
            temp = K // arr[i]
            ans += temp
            K -= temp * arr[i]
print(ans)