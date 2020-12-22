def solution(s):
    s = list(s)
    stack = []
    for i in range(len(s)):
        if len(stack)==0:
            stack.append(s[i])
        elif s[i] == "(":
            stack.append(s[i])
        elif stack[-1] == "(" and s[i] == ")":
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False