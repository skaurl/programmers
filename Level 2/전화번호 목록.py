def solution(phone_book):
    phone_book = sorted(phone_book)
    answer = True
    i = 1
    while True:
        try:
            if phone_book[0] in phone_book[i][:len(phone_book[0])]:
                answer = False
                break
            i+=1
            del phone_book[0]
        except:
            break
    return answer