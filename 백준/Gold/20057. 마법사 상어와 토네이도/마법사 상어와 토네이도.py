import math

def tornado(dir, si, sj, origin):
    global lst
    a, out = origin, 0

    for percent in sand_dir:
        sand = math.floor(origin * percent * 0.01)
        for di, dj in sand_dir[percent]:
            if dir % 2:
                if dir == 1:
                    ni, nj = si + dj * (-1), sj + di
                else:
                    ni, nj = si + dj, sj + di
            else:
                if dir == 2:
                    ni, nj = si + di, sj + dj * (-1)
                else:
                    ni, nj = si + di, sj + dj
            
            if percent == 0:
                sand = a

            if 0 <= ni < N and 0 <= nj < N:
                lst[ni][nj] += sand
            else:
                out += sand
            a -= sand
    lst[ci][cj] = 0
    return out



N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ci = cj = (N // 2)
ans = d = flag = 0
num = 1
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
sand_dir = {1: [(1, 0), (-1, 0)], 2: [(-2, -1), (2, -1)], 7: [(-1, -1), (1, -1)], 10: [(-1, -2), (1, -2)], 5: [(0, -3)], 0: [(0, -2)]}

while ci != 0 or cj != 0:
    for _ in range(2):
        for _ in range(num):
            if ci == 0 and cj == 0:
                flag = 1
                break
            else:
                ni, nj = ci + di[d], cj + dj[d]
                ans += tornado(d, ci, cj, lst[ni][nj])
                ci, cj = ni, nj
        if flag:
            break
        d = (d + 1) % 4
    num += 1

print(ans)