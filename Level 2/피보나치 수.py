def solution(n):
    a = [0, 1, 1]
    if n<=2:
        return a[n]
    else:
        for i in range(3,n+1):
            a.append(a[i-1] + a[i-2])
    return a[n]%1234567