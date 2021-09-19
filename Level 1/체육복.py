def solution(n, lost, reserve):
    Lost = set(lost) - set(reserve)
    Reserve = set(reserve) - set(lost)
    for i in Reserve:
        if i-1 in Lost:
            Lost.remove(i-1)
        elif i+1 in Lost:
            Lost.remove(i+1)
    return n - len(Lost)