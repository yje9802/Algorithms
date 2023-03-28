def solution(s):
    answer = 0
    
    start = 1
    different = 0
    i = 0
    while True:
        if i == len(s)-1:
            answer += 1
            break
        else:
            first = s[0]
            if s[i+1] == first:
                start += 1
            else:
                different += 1
            if start == different:
                if i+2 <= len(s) - 1:
                    answer += 1
                    s = s[i+2:]
                    
                    start = 1
                    different = 0
                    i = 0
                else:
                    answer += 1
                    break
            else:
                i += 1       
    
    return answer