import collections

def solution(clothes):
    clothes = [i[1] for i in clothes]
    clothes = collections.Counter(clothes)
    answer = 1
    clothes = dict(clothes)
    for i in clothes.values():
        answer*=(i+1)
    answer-=1
    return answer