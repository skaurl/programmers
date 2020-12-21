def solution(n):
    answer = 0
    for i in range(n+1,1000001):
        if list(asdf(n)).count("1") == list(asdf(i)).count("1"):
            answer = i
            break
    return answer

def asdf(n):
    n+=1
    if n<=2:
        return "01"[n-1]
    else:
        q, r = divmod(n-1, 2)
        return asdf(q) + "01"[r]