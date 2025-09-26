def solution(money):
    answer = 0
    
    dp_yes = [0] * len(money) # 첫 번째 집을 털었을 경우
    dp_no = [0] * len(money) # 첫 번째 집을 털지 않았을 경우
    
    dp_yes[0] = money[0]
    for i in range(1, len(money)-1):
        dp_yes[i] = max(dp_yes[i-1], dp_yes[i-2] + money[i])
    
    for i in range(1, len(money)):
        dp_no[i] = max(dp_no[i-1], dp_no[i-2] + money[i])
    
    answer = max(dp_yes[-2], dp_no[-1])
    return answer