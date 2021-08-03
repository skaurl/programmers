def solution(price, money, count):
    tmp = price * count * (count + 1) // 2
    if tmp > money:
        return tmp - money
    else:
        return 0