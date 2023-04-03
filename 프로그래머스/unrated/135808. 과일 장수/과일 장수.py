def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    i = 0
    while True:
        if i + m <= len(score):
            dummy = score[i:i+m]
            answer = answer + dummy[-1] * m
            i = i + m
        else:
            break
    
    return answer