import heapq

def format_time(length, type):
    global trains
    platform = []
    for _ in range(length):
        start, end = input().split()
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))
        platform.append((start_hour * 60 + start_minute, end_hour * 60 + end_minute))
        if type == 'A':
            trains.append(((end_hour * 60 + end_minute, start_hour * 60 + start_minute, 'A')))
        else:
            trains.append(((end_hour * 60 + end_minute, start_hour * 60 + start_minute, 'B')))
    return platform

def same_train(type, curr_end):
    global platform_a, platform_b
    end = -1
    if type == 'A':
        for next_start, next_end in platform_b:
            if curr_end <= next_start:
                end = next_end + T
                platform_b.remove((next_start, next_end))
                break 
        if end != -1:
            same_train('B', end)
    else:
        for next_start, next_end in platform_a:
            if curr_end <= next_start:
                end = next_end + T
                platform_a.remove((next_start, next_end))
                break 
        if end != -1:
            same_train('A', end)

def sol(q):
    global start_a, start_b
    heapq.heapify(q)
    while q:
        curr_end, curr_start, type = heapq.heappop(q)
        if type == 'A':
            if (curr_start, curr_end) in platform_a:
                start_a += 1
                same_train('A', curr_end + T)
        else:
            if (curr_start, curr_end) in platform_b:
                start_b += 1
                same_train('B', curr_end + T)

N = int(input())
for tc in range(N):
    T = int(input())
    NA, NB = map(int, input().split())
    start_a = start_b = 0
    trains = []
    platform_a = sorted(format_time(NA, 'A'), key=lambda a: (a[1], a[0]))  # [(540, 720), (660, 750), (600, 780)]
    platform_b = sorted(format_time(NB, 'B'), key=lambda a: (a[1], a[0]))  # [(540, 630), (722, 900)]
    sol(trains)
    print(f'Case #{tc + 1}: {start_a} {start_b}')