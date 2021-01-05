from itertools import product

def solution(numbers, target):
    lst = [[-i,i] for i in numbers]
    return [sum(i) for i in product(*lst)].count(target)