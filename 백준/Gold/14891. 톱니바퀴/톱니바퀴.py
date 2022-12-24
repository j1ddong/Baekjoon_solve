from collections import deque

state = [deque(list(map(int, input().strip()))) for _ in range(4)]

K = int(input())
for _ in range(K):
    number, direction = map(int, input().split())
    number -= 1

    origin = []
    for i in range(4):
        origin.append((state[i][2], state[i][6]))

    state[number].rotate(direction)

    if number != 0: # left
        for i in range(number, 0, -1):
            if origin[i][1] != origin[i - 1][0]:
                if (number - (i - 1)) % 2:
                    state[i - 1].rotate(-1 * direction)
                else:
                    state[i - 1].rotate(direction)
            else:
                break

    if number != 3: # right
        for i in range(number, 3):
            if origin[i][0] != origin[i + 1][1]:
                if (number - (i + 1)) % 2:
                    state[i + 1].rotate(-1 * direction)
                else:
                    state[i + 1].rotate(direction)
            else:
                break

ans = 0
for i in range(4):
    if state[i][0]:
        ans += 2 ** i
print(ans)