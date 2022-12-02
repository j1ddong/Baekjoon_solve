def crashing(m, n, board):
    crashed = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != -1:
                crashed |= set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
    for i, j in crashed:
        board[i][j] = 0
    for idx, row in enumerate(board):
        zero_cnt = row.count(0)
        board[idx] = [-1] * zero_cnt + [origin for origin in row if origin != 0]
    return len(crashed)
    

def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while True:
        crashed_num = crashing(n, m, board)
        if crashed_num == 0:
            return answer
        answer += crashed_num


