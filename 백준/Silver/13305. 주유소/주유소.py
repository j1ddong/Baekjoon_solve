N = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

oil = oils[0]
ans = roads[0] * oils[0]

for i in range(1, N - 1):
    if oils[i] < oil:
        oil = oils[i]
    ans += roads[i] * oil

print(ans)