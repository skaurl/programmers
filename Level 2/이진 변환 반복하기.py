def solution(s):
    count = 0
    count_0 = 0
    while s != "1":
        count_0 += len(s)
        s = s.replace("0","")
        count_0 -= len(s)
        s = asdf(len(s))
        count += 1
    return [count,count_0]

def asdf(n):
    if n<=1:
        return "01"[n]
    else:
        q, r = divmod(n, 2)
        return asdf(q) + "01"[r]