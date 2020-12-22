def solution(citations):
    citations = sorted(citations)
    answer = []
    try:
        for i in range(max(citations)+1):
            c = 0
            for j in citations:
                if i <= j:
                    c+=1
            if i >= c:
                answer.append(c)
        return max(answer)
    except:
        return 0