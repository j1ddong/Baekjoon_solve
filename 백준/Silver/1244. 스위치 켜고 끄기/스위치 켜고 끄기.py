switchLen = int(input())
arr = [0] + list(map(int, input().split()))
studentLen = int(input())

def onOff(arr, gener, number):
    if gener == 1:
        for i in range(number, switchLen + 1, number):
            arr[i] = 0 if(arr[i] == 1) else 1
    else:
        fi = bi = number
        arr[fi] = 0 if(arr[fi] == 1) else 1
        while True:
            fi, bi = fi - 1, bi + 1
            if fi < 1 or bi > switchLen:
                return
            if arr[fi] != arr[bi]:
                return
            arr[fi] = 0 if(arr[fi] == 1) else 1
            arr[bi] = arr[fi]

for _ in range(studentLen):
    gender, number = map(int, input().split())
    onOff(arr, gender, number)

arr = arr[1:]
for l in range(0, switchLen, 20):
    print(*arr[l:l + 20])