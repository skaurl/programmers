def solution(n, m):
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
    return answer