def fish_move():
    new_fish_info = []
    for fi, fj, d in fish_info:
        cnt = 0
        while True:
            ni, nj  = fi + di[d], fj + dj[d]
            if ni < 1 or nj < 1 or ni > 4 or nj > 4 or (ni == si and nj == sj) or MAP[ni][nj] < 0:
                d = (d - 1) % 8
                cnt += 1
            else:
                new_fish_info.append([ni, nj, d])
                break
            if cnt >= 8:
                new_fish_info.append([fi, fj, d])
                break
    return new_fish_info

def make_fish_map(lst):
    new = [[0] * 5 for _ in range(5)]
    for fi, fj, _ in lst:
        new[fi][fj] += 1
    return new

def shark_dir(ci, cj, cnt, turn, memo):
    global navi, kill
    if turn > 2:
        if cnt > kill:
            navi, kill = memo, cnt
        return
    for i in range(4):
        ni, nj = ci + sdi[i], cj + sdj[i]
        if 0 < ni < 5 and 0 < nj < 5:
            if FISH[ni][nj]:
                origin, FISH[ni][nj] = FISH[ni][nj], 0
                shark_dir(ni, nj, cnt + origin, turn + 1, memo + str(i))
                FISH[ni][nj] = origin
            else:
                shark_dir(ni, nj, cnt, turn + 1, memo + str(i))
    
def shark_move(si, sj, navi):
    for d in navi:
        si, sj = si + sdi[int(d)], sj + sdj[int(d)]
        if FISH[si][sj]:
            FISH[si][sj] = 0
            MAP[si][sj] = -3
    return si, sj

def alive_fish(fish):
    alive = []
    for fi, fj, d in fish:
        if FISH[fi][fj]:
            alive.append([fi, fj, d])
    return alive

def heal():
    for i in range(1, 5):
        for j in range(1, 5):
            if MAP[i][j] < 0:
                MAP[i][j] += 1

M, S = map(int, input().split())
MAP = [[0] * 5 for _ in range(5)]
FISH = [[0] * 5 for _ in range(5)]
fish_info = []
for _ in range(M):
    fi, fj, d = map(int, input().split())
    fish_info.append([fi, fj, d - 1])
    FISH[fi][fj] += 1

si, sj = map(int, input().split())

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
sdi = [-1, 0, 1, 0]
sdj = [0, -1, 0, 1]

for _ in range(S):
    navi, kill = '', -1
    new_fish_info = fish_move()
    FISH = make_fish_map(new_fish_info)

    shark_dir(si, sj, 0, 0, '')
    si, sj = shark_move(si, sj, navi)
    new_fish_info = alive_fish(new_fish_info)

    heal()

    new_fish_info += fish_info
    fish_info = new_fish_info

print(len(fish_info))