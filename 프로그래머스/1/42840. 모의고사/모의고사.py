def solution(answers):
    answer = []
    one, two, three = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1, a2, a3 = 0, 0, 0
    
    for i in range(len(answers)):
        i1 = i % 5
        i2 = i % 8
        i3 = i % 10
        
        if one[i1] == answers[i]: a1 += 1
        if two[i2] == answers[i]: a2 += 1
        if three[i3] == answers[i]: a3 += 1
        
    max_one = max(a1, a2, a3)
    if a1 == max_one:
        answer.append(1)
    if a2 == max_one:
        answer.append(2)
    if a3 == max_one:
        answer.append(3)
    
    return answer
