import heapq

def mixDishes(array, k):
    answer = 0
    while 1:
        try:
            newDishValue = heapq.heappop(array) + heapq.heappop(array)*2
            heapq.heappush(array, newDishValue)
            answer += 1
            if array[0] >= k:
                return answer
        except:
            return -1

def solution(array, k):
    heapq.heapify(array)
    answer = mixDishes(array, k)
    return answer