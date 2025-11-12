def solution(cookie):
    answer = 0
    
    for i in range(len(cookie)-1):
        left, right = i, i+1
        left_cookie, right_cookie = cookie[i], cookie[i+1]
        
        while True:
            if left_cookie == right_cookie and left_cookie > answer:
                answer = left_cookie
            if left > 0 and left_cookie <= right_cookie:
                # 왼쪽 쿠키 늘려주기
                left -= 1
                left_cookie += cookie[left]
            elif right < len(cookie)-1 and left_cookie >= right_cookie:
                # 오른쪽 쿠키 늘려주기
                right += 1
                right_cookie += cookie[right]
            else:
                break
                
    return answer