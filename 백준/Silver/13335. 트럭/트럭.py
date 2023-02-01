import sys
input = sys.stdin.readline

N, L, W = map(int, input().split())
trucks = list(map(int, input().split()))
road = [0] * L
cnt, idx = 1, 1
road[-1] = trucks[0]

while True:
    if idx == N and sum(road) == 0:
        break

    cnt += 1
    for i in range(1, L):
        road[i - 1] = road[i]
    road[-1] = 0

    if idx < N and trucks[idx] + sum(road) <= W:
        road[-1] = trucks[idx]
        idx += 1

print(cnt)