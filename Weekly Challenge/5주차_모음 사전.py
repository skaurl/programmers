from itertools import product

def solution(word):
    return sorted(set([''.join(i).replace(' ','') for i in product(*[' AEIOU']*5)])).index(word)