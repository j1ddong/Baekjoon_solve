def calculate(number):
    global pc, pc, adder
    pc = (pc + 1) % 32
    order, operand = number // 32, number % 32
    if order == 0:
        memory[operand] = adder
    elif order == 1:
        adder = memory[operand]
    elif order == 2:
        if adder == 0:
            pc = operand
    elif order == 4:
        adder = (adder + 255) % 256
    elif order == 5:
        adder = (adder + 1) % 256
    elif order == 6:
        pc = operand
    elif order == 7:
        return False
    return True

while True:
    pc = adder = 0
    try:
        memory = [int(input(), 2) for _ in range(32)]
        while True:
            if not calculate(memory[pc]):
                break

        for i in range(7, -1, -1):
            print((adder >> i) & 1, end='')
        print()
    except:
        break