def solution(s):
    s = [map(int,i.split(',')) for i in sorted(s[2:-2].split("},{"), key = lambda x: len(x))]
    answer = []
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer