def solution(begin, target, words):
    length = len(begin)
    if target not in words:
        return 0
    candidates = [(begin, 0)]
    while candidates:
        candidate, cnt = candidates.pop()
        print(candidate, cnt)
        for word in words:
            differ = 0
            for i in range(length):
                if word[i] != candidate[i]:
                    differ += 1
            if differ == 1:
                if word == target:
                    return cnt + 1
                candidates.append((word, cnt + 1))
                words.remove(word)
    return 0