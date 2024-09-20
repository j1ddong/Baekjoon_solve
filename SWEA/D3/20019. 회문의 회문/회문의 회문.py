def isPalindrome(w):
    l = len(w)
    mid = len(w) // 2
    for i in range(mid):
        if w[i] != w[l - i - 1]:
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    word = input()
    N = len(word)
    idx = N // 2
    left, right = word[0:idx], word[-idx:]
    if isPalindrome(left) and isPalindrome(right) and isPalindrome(word):
        print(f'#{tc} YES')
        continue
    print(f'#{tc} NO')