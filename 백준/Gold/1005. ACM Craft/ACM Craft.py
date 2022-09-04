import sys
from collections import deque
input = sys.stdin.readline


def bfs_():
    q = deque()
    for i in range(1, N + 1):
        if not degree[i]:
            q.append(i)
            # 진입차수가 0이므로 바로 dp에 저장가능
            memo[i] = times[i]
    while q:
        now = q.popleft()
        for nelem in order[now]:
            # now > nelem으로 가는 진입차수 -- 
            degree[nelem] -= 1  

            memo[nelem] = max(memo[now] + times[nelem], memo[nelem])

            if not degree[nelem]:
                q.append(nelem)
        


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    order = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    memo = [0] * (N + 1)
    for _ in range(K):
        x, y = map(int, input().split())
        order[x].append(y)
        # x > y 방향이니깐 진입차수 ++
        degree[y] += 1
    W = int(input())
    bfs_()
    print(memo[W])