def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            count = 0
        elif count%2 == 0:
            answer += s[i].upper()
            count += 1
        elif count%2 == 1:
            answer += s[i].lower()
            count += 1
    return answer