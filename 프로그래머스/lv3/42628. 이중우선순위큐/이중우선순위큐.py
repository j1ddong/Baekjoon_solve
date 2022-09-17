import heapq

def solution(operations):
    min_arr = []
    max_arr = []
    for elem in operations:
        if elem[0] == 'I':
            order, data = elem.split()
            heapq.heappush(min_arr, int(data))
            heapq.heappush(max_arr, (-int(data), int(data)))
        elif not len(min_arr):
            continue
        elif elem == 'D -1':
            min_value = heapq.heappop(min_arr)
            max_arr.remove((-min_value, min_value))
        elif elem == 'D 1':
            max_value = heapq.heappop(max_arr)[0]
            min_arr.remove(-max_value)
    if min_arr:
        return [heapq.heappop(max_arr)[1], heapq.heappop(min_arr)]
    else:
        return [0, 0]

