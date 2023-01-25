def sol(ci, cj, csum):
    global ans
    if cj == M:
        ci += 1
        cj = 0
    
    if ci == N:
        ans = max(ans, csum)
        return 

    if not visited[ci][cj]:
        temp = arr[ci][cj] * 2
        for i in range(4):
            di1, dj1, di2, dj2 = b_dict[i]
            ni1, nj1, ni2, nj2 = ci + di1, cj + dj1, ci + di2, cj + dj2
            if ni1 < 0 or ni2 < 0 or nj1 < 0 or nj2 < 0 or ni1 >= N or ni2 >= N or nj1 >= M or nj2 >= M or visited[ni1][nj1] or visited[ni2][nj2]:
                continue
            nsum = temp + arr[ni1][nj1] + arr[ni2][nj2]
            visited[ni1][nj1] = visited[ni2][nj2] = visited[ci][cj] = 1
            sol(ci, cj + 1, csum + nsum)
            visited[ni1][nj1] = visited[ni2][nj2] = visited[ci][cj] = 0
    sol(ci, cj + 1, csum)
        


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
b_dict = [[-1, 0, 0, 1], [-1, 0, 0, -1], [0, -1, 1, 0], [0, 1, 1, 0]]
ans = 0
sol(0, 0, 0)
print(ans)