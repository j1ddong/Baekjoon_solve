def find_mid(start, target, end):
    if start < target < end:
        if target == start + 1:
            print('m')
        else:
            print('o')
        return True
    else:
        return False


N = int(input())
long = [3]
count, i = 3, 1

while count < N:
    count = count * 2 + (i + 3)
    i += 1
    long.append(count)

curr_idx = len(long) - 1
mid = long[curr_idx - 1]

while not find_mid(mid, N, mid + curr_idx + 4):
    if N < 0:
        break
    N -= (mid + curr_idx + 3)
    if 0 < N < 4:
        if N == 1:
            print('m')
        else:
            print('o')
        break

    for i in range(1, len(long)):
        if long[i-1] < N <= long[i]:
            curr_idx = i
            break
    mid = long[curr_idx - 1]