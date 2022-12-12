from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    idx_numbers = [[numbers[i], i] for i in range(N)]
    cnt = 0

    queue = deque(idx_numbers)
    while True:
        max_number = max(queue)
        curr, idx = queue.popleft()
        if curr == max_number[0]:
            cnt += 1
            if idx == M:
                print(cnt)
                break
        else:
            queue.append([curr, idx])