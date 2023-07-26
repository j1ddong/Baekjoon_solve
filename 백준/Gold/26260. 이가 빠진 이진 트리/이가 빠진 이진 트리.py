def post_order(start, length):
    if length == 1:
        print(numbers[start], end=" ")
        return
    mid = length // 2
    post_order(start, mid)
    post_order(start + mid + 1, mid)
    print(numbers[start + mid], end=" ")

N = int(input())
numbers = list(map(int, input().split()))
X = int(input())

numbers.remove(-1)
numbers.append(X)
numbers.sort()
post_order(0, N)