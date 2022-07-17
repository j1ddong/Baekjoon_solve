def order(node):
    pre_lst.append(node)
    if tree[node][0] != '.':
        order(tree[node][0])
    in_lst.append(node)
    if tree[node][1] != '.':
        order(tree[node][1])
    post_lst.append(node)



tree = dict()
N = int(input())
for _ in range(N):
    p, c1, c2 = input().split()
    tree.setdefault(p, [c1, c2])

pre_lst = []
in_lst = []
post_lst = []
order('A')
for elem in pre_lst:
    print(elem, end='')
print()
for elem in in_lst:
    print(elem, end='')
print()
for elem in post_lst:
    print(elem, end='')