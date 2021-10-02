import math

def solution(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])
    answer = []
    stack = []
    for i in range(len(progresses)):
        if len(stack) == 0 or stack[-1] < progresses[i]:
            stack.append(progresses[i])
            answer.append(1)
        else:
            answer[-1] += 1
    return answer