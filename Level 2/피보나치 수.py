def solution(n):
    answer = [0,1]
    for i in range(1,n):
        answer.append((answer[i-1]+answer[i])%1234567)
    return answer[n]