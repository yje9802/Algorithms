def solution(t, p):
    p_len = len(p) 
    answer = 0
    for i in range(len(t)):
        if i + p_len > len(t):
            break
        partial = t[i:i+p_len]
        if partial <= p:
            answer += 1
    
    return answer