def solution(scores):
    answer = ''
    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores[i])):
            tmp.append(scores[j][i])
        if tmp.count(scores[i][i]) == 1 and (scores[i][i] == min(tmp) or scores[i][i] == max(tmp)):
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