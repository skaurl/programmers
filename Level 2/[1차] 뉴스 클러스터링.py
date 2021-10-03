from collections import Counter

def solution(str1, str2):
    STR1 = Counter([(str1[i]+str1[i+1]).lower() for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha()])
    STR2 = Counter([(str2[i]+str2[i+1]).lower() for i in range(len(str2)-1) if (str2[i]+str2[i+1]).isalpha()])
    try:
        return int(len(list((STR1 & STR2).elements())) / len(list((STR1 | STR2).elements())) * 65536)
    except:
        return 65536