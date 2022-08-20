from heapq import heappop, heappush

N, K = map(int, input().split())
max_number = 100001
arr = [max_number] * 100001
arr[N] = 0

def dijkstra(start):
    q = [(0, start)]
    while q:
        sec, now = heappop(q)
        if now == K:
            print(sec)
            break
        if now * 2 < 100001 and arr[now * 2] > sec:
            arr[now * 2] = sec
            heappush(q, (sec, now * 2))
        if now + 1 < 100001 and arr[now + 1] > sec:
            arr[now + 1] = sec
            heappush(q, (sec + 1, now + 1))
        if 0 <= now - 1 and arr[now - 1] > sec:
            arr[now - 1] = sec
            heappush(q, (sec + 1, now - 1))
        


dijkstra(N)