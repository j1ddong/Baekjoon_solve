def solution(s):
    cnt = cnt_zero = 0
    while s != "1":
        after_s_len = len(s.replace('0', ''))
        cnt_zero += len(s) - after_s_len
        cnt += 1
        s = format(int(after_s_len), 'b')
    return [cnt, cnt_zero]