def find_one_color(l, si, ei, sj, ej):
    global white, blue
    temp = 0
    for i in range(si, ei):
        temp += sum(arr[i][sj:ej])
    if l * l == temp:
        blue += 1
    elif temp == 0:
        white += 1
    else:
        l //= 2
        find_one_color(l, si, si + l, sj, sj + l)
        find_one_color(l, si, si + l, sj + l, ej)
        find_one_color(l, si + l, ei, sj, sj + l)
        find_one_color(l, si + l, ei, sj + l, ej)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = blue = 0

find_one_color(N, 0, N, 0, N)
print(white)
print(blue)