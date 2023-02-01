import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
know_num, *know_arr = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]

cnt = 0

visited = [0] * (N + 1)
q = deque(know_arr)
for person in know_arr:
    visited[person] = 1

while q:
    curr = q.popleft()
    for party in parties:
        num, *lst = party
        for person in know_arr:
            if person in lst:
                for p in lst:
                    if not visited[p]:
                        visited[p] = 1
                        q.append(p)
                        know_arr.append(p)
                break

for party in parties:
    num, *lst = party
    for person in know_arr:
        if person in lst:
            break
    else:
        cnt += 1
print(cnt)