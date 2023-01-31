import sys
input = sys.stdin.readline

def grow_one(day):
    i, j = M - 1, 1
    for elem in [0, 1, 2]:
        for _ in range(day[elem]):
            if i >= 0:
                arr[i][0][0] += elem
                arr[i][0][1] = elem
                i -= 1
            else:
                arr[0][j][0] += elem
                arr[0][j][1] = elem
                j += 1

def grow_two():
    for i in range(1, M):
        for j in range(1, M):
            max_num = 0
            for di, dj in [(0, -1), (-1, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                max_num = max(max_num, arr[ni][nj][1])
            arr[i][j][0] += max_num
            arr[i][j][1] = max_num


M, N = map(int, input().split())
arr = [[[1, 0] for _ in range(M)] for _ in range(M)]
days = [list(map(int, input().split())) for _ in range(N)]

for day in days:
    grow_one(day)
    grow_two()

for i in range(M):
    for j in range(M):
        print(arr[i][j][0], end=' ')
    print()
