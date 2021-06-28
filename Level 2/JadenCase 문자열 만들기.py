def solution(s):
    answer = []
    for i in s.split(' '):
        try:
            tmp = i[0].upper() + i[1:].lower()
        except:
            tmp = ''
        answer.append(tmp)
    return ' '.join(answer)