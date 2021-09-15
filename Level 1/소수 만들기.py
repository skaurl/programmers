from itertools import combinations

def prime(n):
    tmp = [False,False] + [True]*(n-1)
    for i in range(2,n+1):
        if tmp[i] == True:
            for j in range(2*i,n+1,i):
                tmp[j] = False
    return [i for i in range(len(tmp)) if tmp[i] == True]

def solution(nums):
    answer = 0
    tmp = [sum(i) for i in combinations(nums,3)]
    tmp_prime = prime(max(tmp))
    for i in tmp:
        if i in tmp_prime:
            answer += 1
    return answer