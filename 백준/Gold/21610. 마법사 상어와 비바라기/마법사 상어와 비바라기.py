def move():
    di = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # 8가지 방향 (인데스 맞추기 위해 맨 처음은 0으로 채움)
    dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    visited = []
    for cloud in clouds:
        ci, cj = cloud[0], cloud[1]
        ni, nj = (ci + di[dk] * si) % N, (cj + dj[dk] * si) % N
        arr[ni][nj] += 1  # 비 내리기
        visited.append([ni, nj])
        check[ni][nj] = 1
    return visited


N, M = map(int, input().split())  # N*N 격자, M은 이동 횟수
arr = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for l in range(M):
    dk, si = map(int, input().split())
    check = [[0] * N for _ in range(N)]
    visited = move()
    for i in range(len(visited)):
        cnt = 0
        for k in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            ni, nj = visited[i][0] + k[0], visited[i][1] + k[1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                cnt += 1
        arr[visited[i][0]][visited[i][1]] += cnt
    clouds = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and check[i][j] == 0:
                clouds.append([i, j])
                arr[i][j] -= 2

print(sum(sum(water) for water in arr))