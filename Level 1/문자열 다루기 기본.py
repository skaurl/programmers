def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            s = int(s)
            answer = True
        except:
            answer = False
    else:
        answer = False
    return answer