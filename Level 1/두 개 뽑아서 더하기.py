def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            print(numbers[i],numbers[j])
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))