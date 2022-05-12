from itertools import permutations, combinations


N = int(input())
K = int(input())
nums = list()
result = set()

for _ in range(N):
    nums.append(input())
selected_nums = combinations(nums, K)
for selected_num in selected_nums:
    for case in permutations(selected_num):
        number = ''.join(case)
        result.add(number)
print(len(result))