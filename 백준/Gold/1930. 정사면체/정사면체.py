import sys
input = sys.stdin.readline
from collections import deque

def sol(arr1, arr2):
    for i in range(4):
        start = [arr1[i]]
        temp = deque([])
        if i % 2:
            di = [1, 3, 2]
        else:
            di = [1, 2, 3]
        for j in di:
            idx = (i + j) % 4
            temp.append(arr1[idx % 4])
        for _ in range(3):
            elem = temp.popleft()
            temp.append(elem)
            candidate = start + list(temp)
            if candidate == arr2:
                return 1            
    return 0

K = int(input())
for _ in range(K):
    a1, a2, a3, a4, b1, b2, b3, b4 = map(int, input().split())
    arr1 = [a1, a2, a3, a4]
    arr2 = [b1, b2, b3, b4]
    print(sol(arr1, arr2))