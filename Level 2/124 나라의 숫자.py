def solution(n):
    answer = ''
    while n > 0:
        q,r = divmod(n-1,3)
        answer += '124'[r]
        n = q
    return answer[::-1]