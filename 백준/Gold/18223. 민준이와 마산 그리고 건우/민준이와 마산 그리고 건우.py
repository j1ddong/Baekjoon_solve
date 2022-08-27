from collections import deque

V, E, P = map(int, input().split())
arr = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

check = [[500000000, 500000000] for _ in range(V + 1)]


def dijkstra(start):
    q = deque([(0, start, False)])
    check[start][0] = 0
    if start == P:
        check[start][1] = 0
        q.append((0, start, True))
    while q:
        w, now, visited = q.popleft()
        for next, nw in arr[now]:
            if visited:
                if check[next][1] > w + nw:
                    check[next][1] = w + nw
                    q.append((w + nw, next, visited))
            else:
                if check[next][0] > w + nw:
                    check[next][0] = w + nw
                    if next == P:
                        q.append((w + nw, next, True))
                        check[next][1] = w + nw
                    else:
                        q.append((w + nw, next, visited))

dijkstra(1)

if check[-1][0] >= check[-1][1]:
    print("SAVE HIM")
else:
    print("GOOD BYE")