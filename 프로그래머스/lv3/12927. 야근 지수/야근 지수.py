import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    arr = []
    for work in works:
        heapq.heappush(arr, -work)
    for i in range(n):
        work = heapq.heappop(arr)
        heapq.heappush(arr, work + 1)
    ans = 0
    for elem in arr:
        ans += elem * elem
    return ans
#     while n != 0:
#         work = max(works)
#         idx = works.index(work)
#         works[idx] -= 1
#         n -= 1
#     ans = 0
#     for work in works:
#         ans += work * work
#     return ans
