K = int(input())
arr = [0, 0] + list(map(int, input().split()))
ans = sum(arr)

for i in range(len(arr) - 1, 2, -2):
    ans += abs(arr[i] - arr[i - 1])
    arr[i // 2] += max(arr[i], arr[i - 1])

print(ans)