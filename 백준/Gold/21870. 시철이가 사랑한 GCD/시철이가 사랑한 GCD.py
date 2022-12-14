import sys
input = sys.stdin.readline

def _gcd(a, b): # 최대 공약수 구하기
    while b > 0:
        a, b = b, a % b
    return a

def gcd(lst):
    ret = lst[0]
    for i in range(1, len(lst)):
        ret = _gcd(ret, lst[i])
    return ret

def find_room(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        l, r = lst[:mid], lst[mid:]
        return max(find_room(r) + gcd(l), find_room(l) + gcd(r))

N = int(input())
rooms = list(map(int, input().split()))
print(find_room(rooms))