def solution(s):
    pc = 0
    yc = 0
    for i in s:
        if "p" == i or "P" == i:
            pc+=1
        if "y" == i or "Y" == i:
            yc+=1

    if pc == yc:
        return True
    elif pc ==0 and yc==0:
        return True
    elif pc != yc:
        return False