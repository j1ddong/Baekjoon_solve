from itertools import combinations

def solution(orders, course):
    answer = []
    for num in course: 
        temp = {}
        max_num = 2
        for order in orders: 
            for elem in combinations(order, num):
                key = ''.join(sorted(elem))
                if temp.get(key):
                    temp[key] += 1
                    max_num = max(max_num, temp[key])
                else:
                    temp[key] = 1
        for key, value in temp.items():
            if value == max_num:
                answer.append(key)
    return sorted(answer)