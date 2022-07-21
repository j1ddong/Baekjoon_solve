N = int(input())
arr = list(map(int, input().split()))
visited = [-2] * N
visited[arr[0]] = -1
cnt = 1

for i in range(1, N):
    if visited[arr[i]] == -2:
        visited[arr[i]] = arr[i - 1]
        cnt += 1
print(cnt)
print(*visited[:cnt])