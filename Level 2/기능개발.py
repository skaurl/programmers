def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        n = 1
        while progresses[i]+n*speeds[i]<100:
            n+=1
        answer.append(n)

    stack = []
    A = []
    for i in range(len(answer)):
        if len(stack)==0:
            stack.append(answer[i])
            A.append(1)
        elif stack[-1]<answer[i]:
            A.append(1)
            stack.append(answer[i])
        else:
            A[-1]+=1
            pass
    return A