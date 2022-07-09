import sys
input = sys.stdin.readline


def DFS(ci, cj, cnt):
    global result
    if cnt > result:
        result = cnt
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < R and 0 <= nj < C and not visited[ord(arr[ni][nj]) - 65]:
            visited[ord(arr[ni][nj]) - 65] = 1
            DFS(ni, nj, cnt + 1)
            visited[ord(arr[ni][nj]) - 65] = 0
        

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [0] * 26
visited[ord(arr[0][0]) - 65] = 1
result = 0
DFS(0, 0, 1)
print(result)