def find_set(x):
    while x != arr[x]:
        x = arr[x]
    return x


def union(x, y):
    arr[find_set(y)] = find_set(x)


def yes_or_no(x, y):
    if find_set(x) == find_set(y):
        return 'YES'
    else:
        return 'NO'
    

n, m = map(int, input().split())
arr = [_ for _ in range(n + 1)]
for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        print(yes_or_no(a, b))
    else:
        union(a, b)