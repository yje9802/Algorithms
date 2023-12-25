def solution(X, Y):
    answer = ''
    
    list_x = [0 for _ in range(0, 10)]
    list_y = [0 for _ in range(0, 10)]
    
    for i in X:
        list_x[int(i)] += 1
    for j in Y:
        list_y[int(j)] += 1
    
    for k in range(0, 10):
        if list_x[k] > 0 and list_y[k] > 0:
            if list_x[k] == list_y[k]:
                answer += str(k) * list_x[k]
            else:
                answer += str(k) * min(list_x[k], list_y[k])
    
    if answer == "": return "-1"
    if answer.replace("0", "") == "": return "0"
    
    answer = sorted(answer, reverse=True)
    answer = "".join(answer)
    return answer