def solution(n):
    n = convert(n,3)
    answer = 0
    for i in range(len(n)):
        answer += int(list(n)[len(n)-1-i])*(3**(len(n)-1-i))
    return answer

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]