def solution(arr1, arr2):
    arr3 = [[0] * len(arr2) for i in range(len(arr2[0]))]

    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]

    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            arr3[j][i] = arr2[i][j]

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] = sum([arr1[i][k]*arr3[j][k] for k in range(len(arr1[i]))])

    return answer