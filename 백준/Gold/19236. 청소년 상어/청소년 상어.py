from copy import deepcopy

def move_fish(fish_dict, arr):
    for num in range(1, 17):
        if fish_dict.get(num):
            ci, cj, cdir = fish_dict[num]
            for d in range(8):
                ndir = (cdir + d) % 8
                di, dj = dirc_dict[ndir]
                ni, nj = ci + di, cj + dj
                if 0 <= ni < 4 and 0 <= nj < 4:
                    if arr[ni][nj] == 0:
                        arr[ni][nj], arr[ci][cj] = num, 0
                        fish_dict[num] = [ni, nj, ndir]
                        break
                    elif arr[ni][nj] > 0:
                        nnum = arr[ni][nj]
                        _, _, temp_dir = fish_dict[nnum]
                        arr[ni][nj], arr[ci][cj] = num, arr[ni][nj]
                        fish_dict[num] = [ni, nj, ndir]
                        fish_dict[nnum] = [ci, cj, temp_dir]
                        break
    return (arr, fish_dict)

def move_shark(ci, cj, cdir, fish_sum, arr, fish_dict):
    global ans
    ni, nj = ci, cj
    for _ in range(4):
        di, dj = dirc_dict[cdir]
        ni, nj = ni + di, nj + dj
        if ni < 0 or nj < 0 or ni > 3 or nj > 3:
            if fish_sum > ans:
                ans = fish_sum
            return 
        if arr[ni][nj] > 0:
            new_arr = deepcopy(arr)
            fish_num = arr[ni][nj]
            next_sum = fish_sum + fish_num
            ndir = fish_dict[fish_num][2]
            new_arr[ni][nj], new_arr[ci][cj] = -1, 0
            new_fish_dict = fish_dict.copy()
            del new_fish_dict[fish_num]
            moved_fish, new_fish_dict = move_fish(new_fish_dict, new_arr)
            move_shark(ni, nj, ndir, next_sum, moved_fish, new_fish_dict)

arr = [[0] * 4 for _ in range(4)]
fish_dict = {}
dirc_dict = {0: (-1, 0), 1: (-1, -1), 2: (0, -1), 3: (1, -1), 4: (1, 0), 5: (1, 1), 6: (0, 1), 7: (-1, 1)}
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(0, 8, 2):
        arr[i][j // 2] = lst[j]
        fish_dict[lst[j]] = [i, j // 2, lst[j + 1] - 1]

ans = 0
fish_num = arr[0][0]
shark_dir = fish_dict[fish_num][2]

arr[0][0] = -1
del fish_dict[fish_num] 
arr, fish_dict = move_fish(fish_dict, arr)
move_shark(0, 0, shark_dir, fish_num, arr, fish_dict)
print(ans)