A, B = input().split()
cnt = 0

if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
else:
    cnt = len(B)
    for i in range(len(B) - len(A) + 1):
        temp = 0
        for j in range(len(A)):
            if A[j] != B[i + j]:
                temp += 1
        cnt = min(cnt, temp)

        
print(cnt)