def solution(a, b):
    m = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    w = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    return w[(sum(m[:a])+b)%7]