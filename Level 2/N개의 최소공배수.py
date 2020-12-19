def solution(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        answer = lcm(arr[0],arr[1])
        return answer
    else:
        answer = lcm(arr[0],arr[1])
        for i in range(2,len(arr)):
            answer = lcm(answer,arr[i])
        return answer

def lcm(n, m):
    answer = []
    M = m
    N = n
    while True:
        if M>=N:
            M = M%N
            if M == 0:
                answer.append(N)
                answer.append(N*(m//N)*(n//N))
                break
        else:
            N = N%M
            if N == 0:
                answer.append(M)
                answer.append(M*(m//M)*(n//M))
                break
    return answer[1]