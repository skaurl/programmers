def solution(n, computers):
    graph = {}
    for i in range(len(computers)):
        graph[str(i)] = set()
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                graph[str(i)].add(str(j))
    answer = 0
    lst = [str(i) for i in range(n)]

    while len(lst) != 0:
        for i in bfs(graph, lst[0]):
            lst.remove(i)
        answer += 1
    return answer

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited