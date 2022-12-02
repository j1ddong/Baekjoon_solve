import sys
input = sys.stdin.readline

def is_palindrom(start, end): 
    if start > end:
        return 1
    if dp[start][end] == -1:
        if numbers[start] == numbers[end]:
            dp[start][end] = is_palindrom(start + 1, end - 1)
        else:
            dp[start][end] = 0
    return dp[start][end]

N = int(input())
numbers = list(input().split())
questions = int(input())

dp = [[-1] * N for _ in range(N)]

for q in range(questions):
    start, end = map(int, input().split())
    print(is_palindrom(start - 1, end - 1))