def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(participant)):
        try:
            if participant[i] != completion[i]:
                return participant[i]
        except:
            return participant[-1]