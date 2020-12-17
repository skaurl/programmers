def solution(s, n):
    answer = ''
    small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
    large = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]
    for i in s:
        if i == " ":
            answer+=" "
        elif i in small:
            answer+=small[(small.index(i)+n)%26]
        elif i in large:
            answer+=large[(large.index(i)+n)%26]
    return answer