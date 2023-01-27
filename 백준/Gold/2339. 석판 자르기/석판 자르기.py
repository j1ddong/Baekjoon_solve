def count_num(si, ei, sj, ej):  
    impurities, jewerly = 0, 0
    for i in range(si, ei):
        for j in range(sj, ej):
            if arr[i][j] == 1:
                impurities += 1
            elif arr[i][j] == 2:
                jewerly += 1
    return impurities, jewerly

def slice_squre(si, ei, sj, ej, direction):
    impurities, jewerly = count_num(si, ei, sj, ej)

    if impurities == 0 and jewerly == 1: 
        return 1
    elif impurities == 1 and jewerly == 1:  # 쥬얼리 없는 칸 생김
        return 0
    elif impurities == 0 and jewerly > 2:  # 쥬얼리 두개
        return 0
    elif jewerly == 0:
        return 0
    
    cnt = 0    
    for i in range(si, ei):
        for j in range(sj, ej):
            if arr[i][j] == 1:
                if direction and i != si and i != ei - 1:
                    for nj in range(sj, ej):
                        if arr[i][nj] == 2:
                            break
                    else:
                        cnt += slice_squre(si, i, sj, ej, 0) * slice_squre(i + 1, ei, sj, ej, 0)
                elif not direction and j != sj and j != ej - 1:
                    for ni in range(si, ei):
                        if arr[ni][j] == 2:
                            break
                    else:
                        cnt += slice_squre(si, ei, sj, j, 1) * slice_squre(si, ei, j + 1, ej, 1)
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
impurities, jewerly = count_num(0, N, 0, N)

ans = slice_squre(0, N, 0, N, 0) + slice_squre(0, N, 0, N, 1)
if impurities == 0 and jewerly == 1:
    print(1)
elif ans:
    print(ans)
else:
    print(-1) 
