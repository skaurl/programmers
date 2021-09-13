def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i == i.lower():
            answer += chr((ord(i)-97+n)%26+97)
        elif i == i.upper():
            answer += chr((ord(i)-65+n)%26+65)
    return answer