N = int(input())
locations = []
people = 0
for _ in range(N):
    l, num = list(map(int, input().split())) 
    people += num
    locations.append([l, num])

locations.sort(key=lambda x: x[0])

curr = 0
for location, num in locations:
    curr += num
    if curr >= people / 2:
        print(location)
        break