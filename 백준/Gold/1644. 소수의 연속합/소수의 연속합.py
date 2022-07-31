def is_prime(number):
    for i in range(2, int(number ** (1/2)) + 1):
        if not number % i:
            return False
    return True

ans = 0
arr = []
N = int(input())
for i in range(2, N + 1):
    if is_prime(i):
        arr.append(i)


startidx = endidx = sum_prime = 0
while True:
    if sum_prime == N:
        ans += 1
    if sum_prime > N:
        sum_prime -= arr[startidx]
        startidx += 1
    elif endidx == len(arr):
        break
    else:
        sum_prime += arr[endidx]
        endidx += 1
print(ans)