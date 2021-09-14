def solution(price, money, count):
    result = sum(range(price,price*count+1,price))-money
    if result <= 0:
        return 0
    return result