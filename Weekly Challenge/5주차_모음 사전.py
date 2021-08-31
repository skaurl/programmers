from itertools import product

def solution(word):
    tmp = [' AEIOU']*5
    answer = sorted(set(''.join(i).replace(' ','') for i in product(*tmp))).index(word)
    return answer