def gcd(n, m):
    n, m = sorted([n, m])
    while n:
        n, m = m % n, n
    return m

def lcm(n, m):
    return n * m // gcd(n, m)

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]