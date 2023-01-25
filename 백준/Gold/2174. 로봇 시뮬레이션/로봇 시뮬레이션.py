def is_make(num, ci, cj, cdir, order, repeat):
    if order == 'L':
        ndir = (cdir - repeat) % 4
        robots_dict[num] = [ci, cj, ndir]
    elif order == 'R':
        ndir = (cdir + repeat) % 4
        robots_dict[num] = [ci, cj, ndir]
    elif order == 'F':
        di, dj = dir_dict[cdir]
        ni, nj = ci, cj
        for _ in range(repeat):
            ni, nj = ni + di, nj + dj
            if ni < 0 or nj < 0 or ni >= B or nj >= A:
                print(f'Robot {num} crashes into the wall')
                return False
            elif arr[ni][nj]:
                print(f'Robot {num} crashes into robot {arr[ni][nj]}')
                return False
        arr[ci][cj], arr[ni][nj] = 0, num
        robots_dict[num] = [ni, nj, cdir]
    return True

A, B = map(int, input().split())
N, M = map(int, input().split())

arr = [[0] * A for _ in range(B)]
dir_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

robots_dict = {}
for idx in range(N):
    i, j, dir = input().split()

    ni, nj = B - int(j), int(i) - 1
    if dir == 'N':
        ndir = 0
    elif dir == 'E':
        ndir = 1
    elif dir == 'S':
        ndir = 2
    elif dir == 'W':
        ndir = 3
    robots_dict[idx + 1] = [ni, nj, ndir]
    arr[ni][nj] = idx + 1

orders = [input().split() for _ in range(M)]

for num, kind, repeat in orders:
    ci, cj, cdir = robots_dict[int(num)]
    if not is_make(int(num), ci, cj, cdir, kind, int(repeat)):
        break
else:
    print('OK')