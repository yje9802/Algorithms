def solution(storey):
    answer = 0
    
    while storey:
        check = storey % 10
        if check > 5: # 6~9
            answer += 10 - check
            storey += 10
        elif check < 5: # 0~4
            answer += check
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += check
        storey //= 10
    return answer