import sys
sys.setrecursionlimit(10**7)


def in_order(node, cnt):
    global last_cnt
    if node != -1:
        in_order(tree[node][0], cnt + 1)
        last_cnt = cnt
        in_order(tree[node][1], cnt + 1)



N = int(input())
tree = [[-1, -1] for _ in range(N + 1)]
result = 2 * (N - 1)
last_cnt = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a][0] = b
    tree[a][1] = c

in_order(1, 0)
print(result - last_cnt)