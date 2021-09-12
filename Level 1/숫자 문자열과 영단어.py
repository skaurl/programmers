def solution(s):
    num_str = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(num_str)):
        s = s.replace(num_str[i],str(i))
    return int(s)