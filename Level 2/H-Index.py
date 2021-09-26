def solution(citations):
    citations = sorted(citations,reverse=True)
    for h in range(len(citations)):
        if citations[h] <= h:
            return h
    return h+1