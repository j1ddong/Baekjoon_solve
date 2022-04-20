N = int(input())  # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 배열
n = int(input())  # 학생 수
for i in range(n):
    S, M = map(int, input().split())
    m = M - 1  # 스위치 있는 숫자랑 인덱스 같아지게 하기
    if S == 1:  # 남자이면
        while m < N:  # m이 스위치 개수보다 작을 때
            if switch[m]:  # 1이면 참이기 때문에 0으로 바꾸기
                switch[m] = 0
            else:
                switch[m] = 1
            m += M  # 배수확인하기 위해서 더해주기, 원래 주어진 숫자 더하기
    else:  # 여자이면
        j = 1
        if switch[m]:  # 주어진 숫자는 무조건 바꾸기
            switch[m] = 0
        else:
            switch[m] = 1
        # 만약 양 옆이 같다면 바꾸고 한칸 더 살펴보기
        while m - j >= 0 and m + j < N and switch[m - j] == switch[m + j]:
            if switch[m - j]:
                switch[m - j] = 0
                switch[m + j] = 0
            else:
                switch[m - j] = 1
                switch[m + j] = 1
            j += 1
for l in range(0, N, 20):
    print(*switch[l:l + 20])
