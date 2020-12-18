def solution(n):
    total = [int(x) for x in list(str(n))]
    total = sum(total)
    if n%total==0:
        return True
    else:
        return False