from collections import defaultdict
# {'ATL': ['ICN', 'SFO'], 'ICN': ['ATL', 'SFO'], 'SFO': ['ATL']}
tickets_dict = defaultdict(list)
answer = []

def DFS(start):
    while tickets_dict[start]:
        a = tickets_dict[start].pop(0)
        DFS(a)
    if not tickets_dict[start]:
        answer.append(start)
        return

def solution(tickets):
    tickets.sort()
    for depature, arrival in tickets:
        tickets_dict[depature].append(arrival)
    DFS('ICN')
    return answer[::-1]