N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

interval = []
for i in range(1, N):
    interval.append(arr[i] - arr[i - 1])

interval.sort()
print(sum(interval[:N - K]))