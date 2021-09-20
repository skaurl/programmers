def Collatz(num):
    if num%2 == 0:
        return num//2
    return 3*num+1

def solution(num):
    answer = 0
    while num != 1:
        num = Collatz(num)
        answer += 1
        if answer == 500:
            return -1
    return answer