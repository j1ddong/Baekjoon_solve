N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))

ans = 1
st, et = arr[0][0], arr[0][1]

for i in range(1, len(arr)):
    if arr[i][0] >= et:
        st, et = arr[i][0], arr[i][1]
        ans += 1

print(ans)