N, D = map(int, input().split())
adjg = [[] for _ in range(D + 1)]
for _ in range(N):
    s, e, w = map(int, input().split())
    if e <= D:
        adjg[s].append((e, w))
min_BFS = [50000] * (D + 1)
min_BFS[0] = 0  # 시작점 0으로 초기화
for i in range(D + 1):
    if min_BFS[i] > min_BFS[i - 1] + 1:
        min_BFS[i] = min_BFS[i - 1] + 1
    if adjg[i]:
        for j in range(len(adjg[i])):
            end, distance = adjg[i][j][0], adjg[i][j][1]
            if min_BFS[end] > min_BFS[i] + distance:
                min_BFS[end] = min_BFS[i] + distance

print(min_BFS[-1])
