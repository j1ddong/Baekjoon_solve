N, M, K = map(int, input().split())

fireball = []
direction = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

for _ in range(K):  
    more = {}
    next = []
    for cx, cy, m, speed, d in fireball: 
        dx, dy = direction[d]
        nx = (cx + dx * speed) % N
        ny = (cy + dy * speed) % N 
        if more.get((nx, ny)):
            om, ospeed, od, cnt_odd, cnt_even, cnt = more[(nx, ny)]
            if cnt == 1:
                next.remove([nx, ny, om, ospeed, od])
            if d % 2: 
                cnt_odd += 1
            else:
                cnt_even += 1
            more[(nx, ny)] = [om + m, ospeed + speed, od, cnt_odd, cnt_even, cnt + 1]
        else:
            cnt_odd = cnt_even = 0
            if d % 2:
                cnt_odd += 1
            else:
                cnt_even += 1
            more[(nx, ny)] = [m, speed, d, cnt_odd, cnt_even, 1]
            next.append([nx, ny, m, speed, d])
    
    fireball = next

    for x, y in more:
        cm, cspeed, cd, cnt_even, cnt_odd, cnt = more[(x, y)]
        nm, nspeed = cm // 5, cspeed // cnt
        if nm and cnt > 1:
            if cnt_even and cnt_odd:
                for nd in (1, 3, 5, 7):
                    fireball.append([x, y, nm, nspeed, nd])
            else:
                for nd in (0, 2, 4, 6):
                    fireball.append([x, y, nm, nspeed, nd])

print(sum([f[2] for f in fireball]))
