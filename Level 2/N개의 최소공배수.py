def gcd(n,m):
    n,m = sorted([n,m])
    while n:
        n,m = m%n,n
    return m

def lcm(n,m):
    return n*m//gcd(n,m)

def solution(arr):
    while len(arr) >= 2:
        arr.append(lcm(arr.pop(),arr.pop()))
    return arr[0]