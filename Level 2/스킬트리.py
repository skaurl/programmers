def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    for i in skill_trees:
        stack = []
        i = list(i)
        for j in i:
            if j in skill:
                stack.append(j)
        for j in range(len(stack)):
            if stack[j] != skill[j]:
                answer += 1
                break
    return len(skill_trees) - answer