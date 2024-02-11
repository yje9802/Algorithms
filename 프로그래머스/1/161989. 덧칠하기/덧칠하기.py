def solution(n, m, section):
    answer = 1
    
    start = section[0]
    for s in range(1, len(section)):
        if section[s] - start >= m:
            start = section[s]
            answer += 1
        
    return answer