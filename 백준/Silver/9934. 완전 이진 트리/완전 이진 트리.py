def tree(start, end, level):
    if start == end:
        ans[level].append(arr[start])
        return
    center = (start + end) // 2
    ans[level].append(arr[center])
    tree(start, center - 1, level + 1)
    tree(center + 1, end, level + 1)



K = int(input())
arr = list(map(int, input().split()))
ans = [[] for _ in range(K)]
l = len(arr)
tree(0, l - 1, 0)
for elem in ans:
    print(*elem)