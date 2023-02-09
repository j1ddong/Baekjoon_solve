import sys
input = sys.stdin.readline

def find_prime(number):
    temp = [1] * len
    for i in range(2, int(number ** (1 / 2)) + 1):
        if temp[i] == 1:
            for j in range(2 * i, len, i):
                temp[j] = 0
                if prime_num[j] == j:
                    prime_num[j] = i


N = int(input())
len = 5_000_001
arr = list(map(int, input().split()))
prime_num = [i for i in range(len)]
find_prime(max(arr))

for elem in arr:
    ans = []
    while elem > 1:
        ans.append(prime_num[elem])
        elem //= prime_num[elem]
    print(*ans)