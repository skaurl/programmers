def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    cnt = 0
    tmp = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    answer[0] = rank[cnt+tmp]
    answer[1] = rank[cnt]
    return answer