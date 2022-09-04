import sys, heapq
input = sys.stdin.readline


N, K = map(int, input().split())
jewelry = []  # [[1, 65], [5, 23], [2, 99]]
bags = []  # [2, 10]
for _ in range(N):
    m ,v = map(int, input().split())
    heapq.heappush(jewelry, [m, v])
for _ in range(K):
    bag = int(input())
    bags.append(bag)
bags.sort()  

stack = []
ans = 0

for bag in bags:
    while jewelry and jewelry[0][0] <= bag:
        weight, value = heapq.heappop(jewelry)
        # 가장 큰 value 구하기 위해 음수로 변환
        heapq.heappush(stack, -value)  
    if stack:
        ans += -heapq.heappop(stack)

print(ans)