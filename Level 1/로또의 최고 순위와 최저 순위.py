def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    return [7 - max(cnt + lottos.count(0), 1), 7 - max(cnt, 1)]