def solution(a, b):
    if a > b:
        answer = sum(list(range(b,a+1,1)))
    elif a < b:
        answer = sum(list(range(a, b+1, 1)))
    else:
        answer = 0
    return answer