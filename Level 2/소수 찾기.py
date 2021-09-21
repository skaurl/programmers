from itertools import permutations

def solution(numbers):
    numbers_lst = []
    for i in range(1, len(numbers) + 1):
        numbers_lst.extend([int(''.join(j)) for j in permutations(numbers, i)])
    numbers_lst = set(numbers_lst)

    TF = [False, False] + [True] * (max(numbers_lst) - 1)
    for i in range(len(TF)):
        if TF[i] == True:
            for j in range(i + i, len(TF), i):
                TF[j] = False
    prime = [i for i in range(len(TF)) if TF[i] == True]

    answer = 0
    for i in numbers_lst:
        if i in prime:
            answer += 1
    return answer