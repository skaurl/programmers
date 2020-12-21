def solution(nums):
    result = [sum(i) for i in comb(nums, 3)]
    total = 0
    Prime = prime(max(result))
    for i in result:
        if i in Prime:
            total+=1
    return total

def comb(lst,n):
    ret = []
    if n>len(lst):
        return ret
    if n==1:
        for i in lst:
            ret.append([i])
    else:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)
    return ret

def prime(n):
    a = [False,False] + [True]*(n-1)
    prime = []
    for i in range(2,n+1):
        if a[i]:
            prime.append(i)
            for j in range(2*i,n+1,i):
                a[j] = False
    return prime