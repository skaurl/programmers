from collections import defaultdict

def solution(clothes):
    tmp_dict = defaultdict(list)
    for i in clothes:
        tmp_dict[i[1]].append(i[0])
    return eval('*'.join([str(len(j)+1) for j in tmp_dict.values()]))-1