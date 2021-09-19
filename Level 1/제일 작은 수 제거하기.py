def solution(arr):
    del arr[arr.index(min(arr))]
    if arr == []:
        arr = [-1]
    return arr