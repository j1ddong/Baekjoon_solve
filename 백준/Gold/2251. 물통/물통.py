from collections import deque


A, B, C = map(int, input().split())  # 8 9 10

water = A + B + C

q = deque([(0, 0)])
visited = [[0] * 201 for  _ in range(201)]
visited[0][0] = 1
result = []

def check(a, b):
    if not visited[a][b]:
        visited[a][b] = 1
        q.append((a, b))

while q:
    a, b = q.popleft()
    c = C - (a + b)
    if a == 0:
        result.append(c)
    pour = min(c, A - a)  # c => a
    check(a + pour, b)
    pour = min(c, B - b)  # c => b
    check(a, b + pour)  
    pour = min(a, B - b)  # a => b
    check(a - pour, b +  pour)
    pour = min(a, C - c)  # a => c
    check(a - pour, b)
    pour = min(b, A - a)  # b => a
    check(a + pour, b - pour)
    pour = min(b, C - c)  # b => c
    check(a, b - pour)

result.sort()
print(*result)