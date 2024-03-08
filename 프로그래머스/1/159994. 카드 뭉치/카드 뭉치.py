def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
        else:
            if len(cards2) > 0 and g == cards2[0]:
                cards2.pop(0)
            else:
                answer = 'No'
                break
        
    return answer