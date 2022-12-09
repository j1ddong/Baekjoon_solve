def solution(files):
    temp = []
    for file in files:
        head = number = tail = ''
        for elem in file:
            if elem.isnumeric():
                if tail:
                    tail += elem
                else:
                    number += elem
            else:
                if number:
                    tail += elem
                else:
                    head += elem
        temp.append([head, number, tail])
    temp.sort(key=lambda i: (i[0].lower(), int(i[1])))
    answer = []
    for elem in temp:
        answer.append(''.join(elem))
    return answer