def solution(answers):
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == math_1[i%len(math_1)]:
            score[0] += 1
        if answers[i] == math_2[i%len(math_2)]:
            score[1] += 1
        if answers[i] == math_3[i%len(math_3)]:
            score[2] += 1
    answer = []
    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)
    return answer