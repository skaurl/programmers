def solution(strings, n):
    A = []
    for i in range(len(strings)):
        A.append((strings[i][n],strings[i]))
    A = sorted(A)
    answer = []
    for i in A:
        answer.append(i[1])
    return answer