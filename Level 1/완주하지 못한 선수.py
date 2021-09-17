def solution(participant, completion):
    participant, completion = sorted(participant), sorted(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]