def solution(n, s, a, b, fares):
    inf = 1e9
    answer = inf
    roads = [[inf] * (n + 1) for _ in range(n + 1)]
    
    for c, d, f in fares:
        roads[c][d] = roads[d][c] = f
    
    for i in range(n + 1):
        roads[i][i] = 0
    
    for i in range(1, n + 1):
        for j in range(1, n  +1):
            for k in range(1, n + 1):
                if roads[j][k] > roads[j][i] + roads[i][k]:
                    roads[j][k] = roads[j][i] + roads[i][k]
    
    for i in range(1, n + 1):
        cost = roads[s][i] +  roads[i][a] + roads[i][b]
        answer = min(answer, cost)
    
    return answer