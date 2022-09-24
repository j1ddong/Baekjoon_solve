def solution(stones, k):
    start, end = 1, max(stones)
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start