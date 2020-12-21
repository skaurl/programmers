def solution(numbers):
    numbers = list(numbers)
    result = []
    total = 0
    for i in range(1,len(numbers)+1):
        for j in perm(numbers,i):
            result.append(int("".join(j)))
    result = list(set(result))
    Prime = prime(max(result))
    for i in result:
        if i in Prime:
            total += 1
    return total

def perm(lst,n):
    ret = []
    if n>len(lst):
        return ret
    if n==1:
        for i in lst:
            ret.append([i])
    else:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp,n-1):
                ret.append([lst[i]]+p)
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

print(solution("011"))