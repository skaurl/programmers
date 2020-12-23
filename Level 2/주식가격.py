def solution(prices):
    answer = []
    for i in range(len(prices)):
        a = prices[i]
        b = 0
        for j in range(i,len(prices)):
            if a <= prices[j]:
                b+=1
            else:
                b+=1
                break
        answer.append(b-1)
    return answer