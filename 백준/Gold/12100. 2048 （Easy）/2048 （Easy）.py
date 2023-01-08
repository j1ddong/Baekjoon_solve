from copy import deepcopy

def up(lst):
    number = 0
    temp = list(map(list, zip(*lst)))
    for i in range(N):
        zero_cnt = temp[i].count(0)
        temp[i] = [i for i in temp[i] if i] + [0] * zero_cnt
    lst = list(map(list, zip(*temp)))
    for i in range(N - 1):
        for j in range(N):
            number = max(number, lst[i][j])
            if lst[i][j] and (lst[i][j] == lst[i + 1][j]):
                lst[i][j], lst[i + 1][j] = lst[i][j] * 2, 0
                number = max(number, lst[i][j])
    temp = list(map(list, zip(*lst)))
    for i in range(N):
        zero_cnt = temp[i].count(0)
        temp[i] = [i for i in temp[i] if i] + [0] * zero_cnt
    new = list(map(list, zip(*temp)))
    return new, number

def down(lst):
    number = 0
    temp = list(map(list, zip(*lst)))
    for i in range(N):
        zero_cnt = temp[i].count(0)
        temp[i] = [0] * zero_cnt + [i for i in temp[i] if i]
    lst = list(map(list, zip(*temp)))
    for i in range(N - 1, 0, -1):
        for j in range(N):
            number = max(number, lst[i][j])
            if lst[i][j] and (lst[i][j] == lst[i - 1][j]):
                lst[i][j], lst[i - 1][j] = lst[i][j] * 2, 0
                number = max(number, lst[i][j])
    temp = list(map(list, zip(*lst)))
    for i in range(N):
        zero_cnt = temp[i].count(0)
        temp[i] = [0] * zero_cnt + [i for i in temp[i] if i]
    new = list(map(list, zip(*temp)))
    return new, number

def left(lst):
    number = 0
    for i in range(N):
        zero_cnt = lst[i].count(0)
        lst[i] = [i for i in lst[i] if i] + [0] * zero_cnt
    for i in range(N):
        for j in range(N - 1):
            number = max(number, lst[i][j])
            if lst[i][j] and (lst[i][j] == lst[i][j + 1]):
                lst[i][j], lst[i][j + 1] = lst[i][j] * 2, 0
                number = max(number, lst[i][j])
    for i in range(N):
        zero_cnt = lst[i].count(0)
        lst[i] = [i for i in lst[i] if i] + [0] * zero_cnt
    return lst, number

def right(lst):
    number = 0
    for i in range(N):
        zero_cnt = lst[i].count(0)
        lst[i] = [0] * zero_cnt + [i for i in lst[i] if i]
    for i in range(N):
        for j in range(N - 1, 0, -1):
            number = max(number, lst[i][j])
            if lst[i][j] and (lst[i][j] == lst[i][j - 1]):
                lst[i][j], lst[i][j - 1] = lst[i][j] * 2, 0
                number = max(number, lst[i][j])
    for i in range(N):
        zero_cnt = lst[i].count(0)
        lst[i] = [0] * zero_cnt + [i for i in lst[i] if i]
    return lst, number

def move(cnt, lst, max_num):
    global ans
    if cnt >= 5:
        if max_num > ans:
            ans = max_num
        return

    if max_num * (2 ** (5 - cnt)) < ans:
        return 

    l_new, l_num = left(deepcopy(lst))
    move(cnt + 1, deepcopy(l_new), l_num)
    r_new, r_num = right(deepcopy(lst))
    move(cnt + 1, deepcopy(r_new), r_num)
    d_new, d_num = down(deepcopy(lst))
    move(cnt + 1, deepcopy(d_new), d_num)
    u_new, u_num = up(deepcopy(lst))
    move(cnt + 1, deepcopy(u_new), u_num)


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 2
if N == 1:
    ans = MAP[0][0]
else:
    move(0, deepcopy(MAP), ans)
print(ans)
