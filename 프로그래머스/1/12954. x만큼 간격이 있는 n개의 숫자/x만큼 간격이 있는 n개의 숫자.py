def solution(x, n):
    answer = []
    increase = 0
    for _ in range(n):
        increase += x
        answer.append(increase)
        
    return answer