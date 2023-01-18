from copy import deepcopy

def sol(idx, arr):
    global ans
    if idx >= len(camera):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    cnt += 1
        ans = max(ans, cnt)
        return
    ci, cj, camera_type = camera[idx]
    if camera_type == 2:
        for i in range(2):
            n_arr = make_new_arr(camera_type, deepcopy(arr), i, ci, cj)
            sol(idx + 1, n_arr)    
    else:
        for i in range(4):
            n_arr = make_new_arr(camera_type, deepcopy(arr), i, ci, cj)
            sol(idx + 1, n_arr)    


def make_new_arr(num, lst, i, ci, cj):
    for di, dj in camera_dir[num][i]:
        ni, nj = ci + di, cj + dj
        while 0 <= ni < N and 0 <= nj < M:
            if lst[ni][nj] == 6:
                break
            if lst[ni][nj] == 0:
                lst[ni][nj] = -1
            ni, nj = ni + di, nj + dj
    return lst


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
camera_dir = {1: [[(-1, 0)], [(1, 0)], [(0, 1)], [(0, -1)]], 2: [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]], 3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]], 4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]]}
ans = 0

camera = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 5:
            camera.append((i, j, arr[i][j]))
        elif arr[i][j] == 5: 
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj  = i + di, j + dj
                while 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == 6:
                        break
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                    ni, nj  = ni + di, nj + dj

sol(0, deepcopy(arr))
print(N * M - ans)