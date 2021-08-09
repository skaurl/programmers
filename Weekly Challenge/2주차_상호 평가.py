def solution(scores):
    answer = ''
    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        if tmp.count(scores[i][i]) == 1:
            if max(tmp) == scores[i][i] or min(tmp) == scores[i][i]:
                del tmp[i]
        avg = sum(tmp)/len(tmp)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer