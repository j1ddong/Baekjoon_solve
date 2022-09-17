def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    num, plus = s // n, s % n
    for _ in range(n):
        answer.append(num)
    idx = n - 1
    for _ in range(plus):
        answer[idx] += 1
        idx -= 1
    return answer
