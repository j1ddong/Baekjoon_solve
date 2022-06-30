N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def DFS(lst):
    ans = 0
    visited = [[0] * N for _ in range(N)]
    for ti, tj in lst:
        if not visited[ti][tj]:
            stack = [(ti, tj)]
            while stack:
                si, sj = stack.pop()
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = si + di, sj + dj
                    if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and not visited[ni][nj] and arr[ni][nj]:
                        stack.append((ni, nj))
                        visited[ni][nj] = 1
            ans += 1
    return ans 


rain = 0
result = 0
while True:
    safe_zone = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                arr[i][j] = 0
            else:
                safe_zone.append((i, j))
    if result < DFS(safe_zone):
        result = DFS(safe_zone)
    if not len(safe_zone):
        break 
    rain += 1
print(result)

    