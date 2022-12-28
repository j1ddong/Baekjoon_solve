def flip(cnt, lst, order, max_num, idx):
    global ans_cnt, ans_order
    if not idx:
        if lst[0] < 0:
            ans_cnt, ans_order = cnt + 1, order + [1]
        else:
            ans_cnt, ans_order = cnt, order
    for i in range(len(lst)):
        if abs(lst[i]) == max_num:
            if i == idx and lst[i] == max_num:
                max_num -= 1
                idx -= 1
                flip(cnt, lst, order, max_num, idx)
            else:
                mark = i + 1
                if i == 0 and lst[i] < 0:
                    mark = idx + 1
                change, stay = lst[:mark], lst[mark:]
                change = list(map(lambda x: x * -1, change[::-1]))
                new_order = order + [mark]
                flip(cnt + 1, change + stay, new_order, max_num, idx)
        

N = int(input())
for _ in range(N):
    M, *lst = list(map(int, input().split()))
    ans_cnt, ans_order = 0, []
    flip(0, lst, [], M, M - 1)
    print(ans_cnt, *ans_order)