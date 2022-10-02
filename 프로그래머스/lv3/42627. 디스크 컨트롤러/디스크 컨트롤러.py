import heapq
def solution(jobs):
    answer = now = i = 0
    ready_queue = []
    start = -1
    while i < len(jobs):
        for income, duration in jobs:
            if start < income <= now:
                heapq.heappush(ready_queue, (duration, income))
        if ready_queue:
            program = heapq.heappop(ready_queue)
            start = now
            now += program[0]
            answer += program[0] + (start - program[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))