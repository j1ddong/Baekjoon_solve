import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in range(N):
    left, right = 0, len(dp) - 1  # 현재까지 찾은 배열의 왼, 오
    while left <= right:  # 이진탐색
        mid = (left + right) // 2
        if dp[mid] < arr[i]:
            left = mid + 1
        else:
            right = mid - 1
    if left >= len(dp):  # dp안에 arr[i]보다 큰 숫자 없음 > 숫자 추가
        dp.append(arr[i])
    else:
        # left: arr[i]에 제일 가까운 값을 가진 인덱스
        dp[left] = arr[i]  # 더 작은 값으로 교체
print(len(dp) - 1)
