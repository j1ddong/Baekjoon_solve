from collections import deque

N, K = input().split()
K = int(K)
M = len(N)


def bfs():
    checked = set()
    checked.add((N, 0))
    q = deque([(N, 0)])
    ans = -1
    while q:
        n, k = q.popleft()
        if k == K:
            ans = max(ans, int(n))
        else:
            lst_n = list(n)
            for i in range(M - 1):
                for j in range(i + 1, M):
                    if i == 0 and lst_n[j] == '0':
                        continue
                    lst_n[i], lst_n[j] = lst_n[j], lst_n[i]
                    new_n = ''.join(lst_n)
                    if (new_n, k + 1) not in checked:
                        q.append((new_n, k + 1))
                        checked.add((new_n, k + 1))
                    lst_n[i], lst_n[j] = lst_n[j], lst_n[i]
    return ans

print(bfs())