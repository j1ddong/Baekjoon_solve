from collections import defaultdict

TC = int(input())
for testcase in range(TC):
    N = int(input())
    arr = [i for i in range(N + 1)]
    num_dict = defaultdict(int)
    for i in range(N - 1):
        p, c = map(int, input().split())
        arr[c] = p
    a, b = map(int, input().split())
    while a != arr[a]:
        num_dict[a] = 1
        a = arr[a]
    num_dict[a] = 1
    while num_dict.get(b) == None:
        b = arr[b]
    ans = b
    print(ans)