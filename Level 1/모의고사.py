def solution(answers):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    p_1 = [1, 2, 3, 4, 5]
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if p_1[i%5] == answers[i%len(answers)]:
            sum_1 += 1

    for i in range(len(answers)):
        if p_2[i%8] == answers[i%len(answers)]:
            sum_2 += 1

    for i in range(len(answers)):
        if p_3[i%10] == answers[i%len(answers)]:
            sum_3 += 1

    if sum_1 == sum_2 == sum_3:
        return [1,2,3]
    elif sum_1 > sum_2 and  sum_1 > sum_3:
        return [1]
    elif sum_2 > sum_1 and  sum_2 > sum_3:
        return [2]
    elif sum_3 > sum_2 and  sum_3 > sum_1:
        return [3]
    elif sum_1 == sum_2 and  sum_1 > sum_3:
        return [1,2]
    elif sum_2 > sum_1 and  sum_2 == sum_3:
        return [2,3]
    elif sum_3 > sum_2 and  sum_3 == sum_1:
        return [1,3]