def solution(n, l, r):
    answer = 0
    
    for i in range(l-1, r):
        x = i
        while x > 0:
            if x % 5 == 2: # 비트값이 0이기 때문
                break
            x //= 5
        else: # break가 없었다면 비트값이 1이라는 의미
            answer += 1
    
    return answer