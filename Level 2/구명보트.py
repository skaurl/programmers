def solution(people, limit):
    people = sorted(people)
    answer = []
    i = 0
    j = len(people)-1
    while i<=j:
        if people[i] + people[j] <= limit:
            i+=1
            answer.append(people[i] + people[j])
        else:
            answer.append(people[j])
        j -= 1
    return len(answer)