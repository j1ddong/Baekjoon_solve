def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[costs[0][0]] = 1
    answer = 0
    while sum(visited) != n: 
        for island1, island2, cost in costs:
            if visited[island1] and visited[island2]:
                continue
            if visited[island1] or visited[island2]:
                visited[island1] = visited[island2] = 1
                answer += cost
                break
    return answer
    # ans = 0
    # visited = set(costs[0][0])  # 시작점
    # while len(visited) != n:
    #     for island1, island2, cost in costs:
    #         if island1 in visited and island2 in visited:
    #             continue
            