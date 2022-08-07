N = int(input())
ans = 1000001

def make_one(number, cnt):
    global ans
    if number == 1:
        ans = min(cnt, ans)
        return
    if cnt >= ans:
        return
    if number % 2 == 0:
        make_one(number // 2, cnt + 1)
    if number % 3 == 0:
        make_one(number // 3, cnt + 1)
    make_one(number - 1, cnt + 1)

make_one(N, 0)
print(ans)
