def solution(s):
    try:
        answer = int(s)
    except:
        answer = -1 * int(s[1:])
    return answer

print(solution(-1234))