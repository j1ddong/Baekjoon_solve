M = int(input())
orders = [list(map(int, input().split())) for _ in range(M)]
locations = [-1, 'A', 'B', 'C']

for a, b in orders:
    locations[a], locations[b] = locations[b], locations[a]

if 0 < locations.index('A') < 4:
    print(locations.index('A'))
else:
    print(-1)