from collections import deque


def BFS():
    CNT = [102 for _ in range(101)]
    q = deque()
    q.append((1, 0))
    while q:
        now, w = q.popleft()
        if now == 100:
            return w
        for i in range(1, 7):
            next = now + i
            if next < 101:
                if MAP[next]:
                    next = MAP[next]
                if CNT[next] > w + 1:
                    CNT[next] = w + 1
                    q.append((next, w + 1))



MAP = [0 for _ in range(101)]
L, S = map(int, input().split())

for _ in range(L):
    x, y = map(int, input().split())
    MAP[x] = y

for _ in range(S):
    u, v = map(int, input().split())
    MAP[u] = v

print(BFS())