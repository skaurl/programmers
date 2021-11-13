def solution(n):
    result = [[0] * n for i in range(n)]
    answer = []
    x, y, num = -1, 0, 1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            result[x][y] = num
            num += 1
    for i in result:
        for j in i:
            if j:
                answer.append(j)
    return answer