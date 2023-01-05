def blizzard(d, s):
    ci = cj = N // 2
    for i in range(1, s + 1):
        ni, nj = ci + di[d] * i, cj + dj[d] * i
        MAP[ni][nj] = 0

def move():
    cx = cy = N // 2
    num = 1
    d = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    balls = []
    while True:
        for _ in range(2):
            for _ in range(num):
                cx, cy = cx + dx[d], cy + dy[d]
                if cx < 0 or cy < 0 or cx >= N or cy >= N:
                    return balls
                if MAP[cx][cy] > 0:
                    balls.append(MAP[cx][cy])
            d = (d + 1) % 4
        num += 1

def bomb(balls):
    old, cnt = -1, 1
    flag = False
    new_ball = []

    for ball in balls:
        if old != ball:
            old = ball
            if cnt >= 4:
                flag = True
                bomb_num[new_ball[-1]] += cnt
                for _ in range(cnt):
                    new_ball.pop()
            cnt = 0
        new_ball.append(ball)
        cnt += 1
    if cnt >= 4:
        flag = True
        bomb_num[new_ball[-1]] += cnt
        for _ in range(cnt):
            new_ball.pop()
    return (new_ball, flag)

def ball_copy(balls):
    if not balls:
        return []

    new = []
    old, cnt = balls[0], 1
    for i in range(1, len(balls)):
        if old != balls[i]:
            new.extend([cnt, old])
            old = balls[i]
            cnt = 1
        else:
            cnt += 1
    new.extend([cnt, old])
    return new

def new_map(balls):
    new = [[0] * N for _ in range(N)]
    if not balls:
        return new
    ci = cj = N // 2
    num = 1
    d = idx = 0
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    while True:
        for _ in range(2):
            for _ in range(num):
                ci, cj = ci + di[d], cj + dj[d]
                if ci < 0 or cj < 0 or ci >= N or cj >= N:
                    return new
                new[ci][cj] = balls[idx]
                idx += 1
                if idx >= len(balls):
                    return new
            d = (d + 1) % 4
        num += 1

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(M)]

bomb_num = [0, 0, 0, 0]

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for dir, s in orders:
    blizzard(dir, s)
    balls = move()
    is_removed = True
    while is_removed:
        new_balls, is_removed = bomb(balls)
        balls = new_balls[:]
    final_balls = ball_copy(new_balls)
    MAP = new_map(final_balls)

ans = 0
for i in range(1, 4):
    ans += bomb_num[i] * i

print(ans)