def tic_tok(t):
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0:
                arr[i][j] += 1
    return t + 1

def new_bomb(t):
    for i in range(R):
        for j in range(C):
            if not arr[i][j]:
                arr[i][j] = -3
            else:
                arr[i][j] += 1
    return t + 1

def explode():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                arr[i][j] = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        arr[ni][nj] = 0



R, C, N = map(int, input().split())
arr = [[0] * C for _ in range(R)]
for i in range(R):
    row = input()
    for j in range(C):
        arr[i][j] = 0 if row[j] == '.' else -3
time = 0
time = tic_tok(time)

while True:
    if time >= N:
        break
    time = new_bomb(time)
    if time >= N:
        break
    explode()
    time = tic_tok(time)
    if time >= N:
        break

for i in range(R):
    temp =  ''
    for j in range(C):
        if arr[i][j] < 0:
            temp += 'O'
        else:
            temp += '.'
    print(temp)