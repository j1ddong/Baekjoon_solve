import sys
from itertools import combinations
input = sys.stdin.readline


N, S = map(int, input().split())
lst = list(map(int, input().split()))

# N이 최대 40이므로 나눠서 탐색
left_arr, right_arr = lst[:N // 2], lst[N // 2:]

subsum1 = []
subsum2 = []

def all_combi_sum(arr, sum_arr):
    for i in range(len(arr) + 1):
        combi = combinations(arr, i)
        for c in combi:
            sum_arr.append(sum(c))

all_combi_sum(left_arr, subsum1)
all_combi_sum(right_arr, subsum2)

subsum1.sort()
subsum2.sort()

left, right, ans = 0, len(subsum2) - 1, 0

while left < len(subsum1) and right >= 0:
    temp = subsum1[left] + subsum2[right]
    if temp == S:
        same_sub_left = 1
        same_sub_right = 1
        
        left += 1
        right -= 1

        while left < len(subsum1) and subsum1[left] == subsum1[left - 1]:
            same_sub_left += 1
            left += 1
        while right >= 0 and subsum2[right] == subsum2[right + 1]:
            same_sub_right += 1
            right -= 1
        ans += same_sub_left * same_sub_right

    elif temp < S:
        left += 1
    else:
        right -= 1

if S == 0:
    ans -= 1

print(ans)