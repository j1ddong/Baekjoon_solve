import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()
start, end, result = 1, houses[-1] - houses[0], 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1

    installed_house = houses[0]
    for i in range(1, N):
        if houses[i] - installed_house >= mid:
            cnt += 1
            installed_house = houses[i]
    
    if cnt >= C:
        result =  max(result, mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)