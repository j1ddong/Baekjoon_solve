N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = ""

def Qtree(l, si, ei, sj, ej, d):
    global ans
    if d == 0:
        ans += "("
    temp = 0
    for i in range(si, ei):
        temp += sum(arr[i][sj: ej])
    if l * l == temp:
        ans += "1"
    elif temp == 0:
        ans += "0"
    else:
        l //= 2 
        Qtree(l, si, si + l, sj, sj + l, 0)
        Qtree(l, si, si + l, sj + l, ej, 1)
        Qtree(l, si + l, ei, sj, sj + l, 2)
        Qtree(l, si + l, ei, sj + l, ej, 3)
    if d == 3:
        ans += ")"

Qtree(N, 0, N, 0, N, 4)
print(ans)
