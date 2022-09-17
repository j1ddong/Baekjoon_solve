def solution(s):
    arr = s.split(' ')
    ans = []
    for elem in arr:
        if elem:
            try:
                int(elem[0])
                temp = elem[0]
            except ValueError:
                temp = elem[0].upper()
            temp += elem[1:].lower()
            ans.append(temp)
        else:
            ans.append(elem)
    return ' '.join(ans)
            