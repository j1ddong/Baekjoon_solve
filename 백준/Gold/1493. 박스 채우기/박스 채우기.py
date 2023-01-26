length, width, height = map(int, input().split())
total = length * width * height

N = int(input())
boxes = []
for _ in range(N):
    i, cnt = map(int, input().split()) 
    boxes.append(((2 ** i), cnt))
boxes.sort(reverse=True)

ans, curr = 0, 0

for box, cnt in boxes:
    curr *= 8
    # 최대로 채운 것 - 이미 채운 것
    cnt_limit = (length // box) * (width // box) * (height // box) - curr
    possible = min(cnt, cnt_limit) 
    ans += possible
    curr += possible

if total == curr:
    print(ans)
else:
    print(-1)