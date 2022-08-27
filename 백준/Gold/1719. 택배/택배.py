from collections import deque


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s1, s2, time = map(int, input().split())
    arr[s1].append((s2, time))
    arr[s2].append((s1, time))


def dijkstra(start):
    checked = [2000001] * n
    ans = ["-"] * n
    q = deque([(0, start, start)])
    checked[start - 1] = 0
    while q:
        weight, first, now = q.popleft()
        for next, time in arr[now]:
            if checked[next - 1] > weight + time:
                checked[next - 1] = weight + time
                if first == start:
                    q.append((checked[next - 1], next, next))
                    ans[next - 1] = next
                else:
                    q.append((checked[next - 1], first, next))
                    ans[next - 1] = first
    print(*ans)

for _ in range(n):
    dijkstra(_ + 1)