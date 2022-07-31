# 부분집합 구하는 함수
def brute_force(l, w, arr_sum, arr_weight):
    if l >= len(arr_weight):
        arr_sum.append(w)
        return
    # 부분집합 경우의 수: 현재 원소 더하거나 더하지 않거나
    brute_force(l + 1, w, arr_sum, arr_weight)
    brute_force(l + 1, w + arr_weight[l], arr_sum, arr_weight)


def binarysearch(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end


N, C = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


a_weight = arr[: N // 2]
b_weight = arr[N // 2 :]

a_sum = []
b_sum = []

brute_force(0, 0, a_sum, a_weight)
brute_force(0, 0, b_sum, b_weight)
# 이진 탐색을 위한 정렬
b_sum.sort()

for i in a_sum:
    # b_sum에 있는 거 집어넣을 수 없다
    if C - i < 0:
        continue
    cnt += binarysearch(b_sum, C - i, 0, len(b_sum))
print(cnt)