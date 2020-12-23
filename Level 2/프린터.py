def solution(priorities, location):
    L = list(range(len(priorities)))
    i = 0
    x = True
    while x:
        try:
            if priorities[i] < max(priorities[i+1:]):
                priorities = priorities[:i] + priorities[i+1:] + [priorities[i]]
                L = L[:i] + L[i+1:] + [L[i]]
            else:
                i += 1
        except:
            break
    return L.index(location)+1

print(solution([1,2,4,2,3], 2))
