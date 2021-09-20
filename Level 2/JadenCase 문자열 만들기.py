def solution(s):
    answer = s.split(' ')
    for i in range(len(answer)):
        if answer[i] != '':
            answer[i] = answer[i][0].upper() + answer[i][1:].lower()
    return ' '.join(answer)