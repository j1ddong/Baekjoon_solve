def solve_tile(restroom, rest, curr):
    global solved
    if solved:
        return
    if not rest:
        for elem in restroom:
            print(*elem)
        solved = True
        return
    for i in range(length):
        for j in range(length):
            if not restroom[i][j]:
                for tile in tiles:
                    cnt = 1
                    for dx, dy in tile:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < length and 0 <= ny < length and not restroom[nx][ny]:
                            cnt += 1
                    if cnt == 3:
                        restroom[i][j] = curr
                        for dx, dy in tile:
                            nx, ny = i + dx, j + dy
                            restroom[nx][ny] = curr
                        solve_tile(restroom, rest - 3, curr +  1)
                        restroom[i][j] = 0
                        for dx, dy in tile:
                            nx, ny = i + dx, j + dy
                            restroom[nx][ny] = 0



K = int(input())
length = 2 ** K
x, y = map(int, input().split())

tiles = [[(0, 1), (-1, 0)], [(0, -1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (1, 0)]]
restroom = [[0] * length for _ in range(length)]

holeX, holeY = length-y, x-1
restroom[holeX][holeY] = -1

rest = length ** 2 - 1
solved = False
solve_tile(restroom, rest, 1)