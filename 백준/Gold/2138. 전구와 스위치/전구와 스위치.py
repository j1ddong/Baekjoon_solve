def sol(origin):
    temp = origin[:]
    cnt = 0
    for i in range(1, N):
        if temp[i - 1] == target[i - 1]:
            continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < N:
                temp[j] = 1 - temp[j]
    return cnt if temp == target else 1e9

N = int(input())
origin = list(map(int, input()))
target = list(map(int, input()))

first_origin = origin[:]
for i in range(2):
    first_origin[i] = 1 - first_origin[i]

candidate1, candidate2 = sol(origin), sol(first_origin)

if candidate1 == candidate2 == 1e9:
    print(-1)
else:
    ans = min(candidate1, candidate2 + 1)
    print(ans)