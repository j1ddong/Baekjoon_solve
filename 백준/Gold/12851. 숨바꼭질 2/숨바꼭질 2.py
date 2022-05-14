from collections import deque


def BFS():
    global sec, count
    q = deque()
    q.append((0, start))
    visited = [0] * 100001
    visited[start] = 0
    while q:
        cnt, now = q.popleft()
        if now == end:
            if sec and sec == cnt:
                count += 1
            if sec == 0:
                sec = cnt
                count += 1
                continue
        visited[now] = 1
        for next in ((now + 1, now - 1, now * 2)):
            if 0 <= next < 100001 and visited[next] == 0:
                q.append((cnt + 1, next))


start, end = map(int, input().split())
sec = count = 0  # 걸린 시간과 도달한 횟수
BFS()        
print(sec)
print(count)
