def solution(begin, target, words):
    words.append(begin)
    graph = {}
    for i in range(len(words)):
        graph[words[i]]=set()
        for j in range(len(words)):
            cnt = 0
            for k in range(len(words[i])):
                if words[i][k]!=words[j][k]:
                    cnt+=1
            if cnt == 1:
                graph[words[i]].add(words[j])
    answer = bfs_path(graph,begin,target)
    if len(answer)==0:
        return 0
    else:
        return len(answer[0])-1

def bfs_path(graph,start,goal):
    queue = [(start,[start])]
    result = []
    while queue:
        n,path = queue.pop(0)
        if n == goal:
            result.append(path)
            return result
        else:
            for m in graph[n]-set(path):
                queue.append((m,path+[m]))
    return result