N = int(input())
graph = [[0] * 101 for _ in range(101)]
plus = [[0, 1], [-1, 0], [0, -1], [1, 0]]
for _ in range(N):
    cj, ci, d, g = list(map(int, input().split())) 
    graph[ci][cj] = 1

    directions = [d]
    for generation in range(g):
        for idx in range(len(directions) - 1, -1, -1):
            directions.append((directions[idx] + 1) % 4)

    for direction in directions:
        ni, nj = ci + plus[direction][0], cj + plus[direction][1]
        if 0 <= ni < 101 and 0 <= nj < 101:
            graph[ni][nj] = 1
        ci, cj = ni, nj

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == graph[i + 1][j] == graph[i][j + 1] == graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)