N = int(input())
start = max(N - 9 * len(str(N)), 0)
ans = 0
for i in range(start, N):
    if N == sum(map(int, str(i))) + i:
        ans = i
        break
if ans == 0 :
    print(0)
else:
    print(ans)