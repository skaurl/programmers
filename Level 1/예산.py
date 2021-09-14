def solution(d, budget):
    d = sorted(d)
    while sum(d) > budget:
        d.pop()
    return len(d)