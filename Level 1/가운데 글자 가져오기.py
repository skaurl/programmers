import math

def solution(s):
    f = math.floor(len(s)/2)
    c = math.ceil(len(s)/2)
    if f == c:
        return s[f-1:c+1]
    return s[f:c]