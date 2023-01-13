def sol():
    for i in range(1, N + 1):
        if is_reach(i):
            return i
    return -1

def is_reach(num):
    s = [num]
    cnt = 0
    while s:
        curr = s.pop()
        for next in graph[curr]:
            s.append(next)
            cnt += 1
    if cnt == N - 1:
        return True
    return False

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[b].append(a)

print(sol())