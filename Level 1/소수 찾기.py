def solution(n):
    tmp = [False,False] + [True]*(n-1)
    for i in range(2,n+1):
        if tmp[i] == True:
            for j in range(2*i,n+1,i):
                tmp[j] = False
    return len([i for i in range(len(tmp)) if tmp[i] == True])