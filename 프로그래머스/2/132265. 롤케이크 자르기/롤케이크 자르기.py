def solution(topping):
    answer = 0
    
    right_toppings = {}
    for t in topping:
        if t in right_toppings:
            right_toppings[t] += 1
        else:
            right_toppings[t] = 1
    right_cnt = len(right_toppings) # 오른쪽 토핑의 개수
    
    left_toppings = {}
    left_cnt = 0 # 왼쪽 토핑의 개수
    for i in range(len(topping)):
        right_toppings[topping[i]] -= 1
        if right_toppings[topping[i]] == 0:
            right_cnt -= 1
        if topping[i] in left_toppings:
            left_toppings[topping[i]] += 1
        else:
            left_toppings[topping[i]] = 1
            left_cnt += 1
        if left_cnt == right_cnt:
            answer += 1
        
    return answer