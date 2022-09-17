def solution(s):
    arr = list(map(int, s.split(' ')))
    max_num, min_num = str(max(arr)), str(min(arr))
    ans = min_num + ' ' + max_num
    return ans