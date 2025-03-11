alphabetArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def get_total_cnt(n):
    return 26 ** n
        
def solution(n, bans):
    cnt = digit = 0
    n_cnt_map = {}
    prefix_count = {}
    
    for ban in bans:
        key = len(ban)
        if n_cnt_map.get(key):
            n_cnt_map[key] += 1
        else:
            n_cnt_map[key] = 1
        
        if key not in prefix_count:
            prefix_count[key] = {}
            
        for i in range(1, len(ban) + 1):
            prefix = ban[:i]
            if prefix not in prefix_count[key]:
                prefix_count[key][prefix] = 0
            prefix_count[key][prefix] += 1
    
    for i in range(1, 12):
        n_total_cnt = get_total_cnt(i) - n_cnt_map.get(i, 0)
        if cnt < n <= n_total_cnt:
            break
        digit = i
        cnt += n_total_cnt

    answer = ''
    for i in range(digit, -1, -1):
        for alphabet in alphabetArr:
            temp_cnt = 0
            if prefix_count.get(digit + 1):
                temp_cnt = prefix_count[digit + 1].get(answer + alphabet, 0)    
            jump_cnt = get_total_cnt(i) - temp_cnt
            
            if cnt + jump_cnt >= n:
                answer += alphabet
                break
            cnt += jump_cnt

    return answer