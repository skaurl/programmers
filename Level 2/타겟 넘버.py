from itertools import product

def solution(numbers, target):
    return [sum(i) for i in product(*[[-i,i] for i in numbers])].count(target)