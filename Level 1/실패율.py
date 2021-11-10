def solution(N, stages):
    answer = {}
    total = len(stages)
    for i in range(1,N+1):
        if total != 0:
            cnt = stages.count(i)
            answer[i] = cnt / total
            total -= cnt
        else:
            answer[i] = 0
    return sorted(answer, key=lambda x : answer[x], reverse=True)