def solution(priorities, location):
    Priorities = list(range(len(priorities)))
    stack = []
    while True:
        if len(priorities) == 1:
            stack.append(Priorities[0])
            break
        elif priorities[0] < max(priorities[1:]):
            priorities = priorities[1:] + [priorities[0]]
            Priorities = Priorities[1:] + [Priorities[0]]
        elif priorities[0] >= max(priorities[1:]):
            stack.append(Priorities[0])
            priorities = priorities[1:]
            Priorities = Priorities[1:]
    return stack.index(location) + 1