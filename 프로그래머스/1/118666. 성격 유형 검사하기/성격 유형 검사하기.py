def solution(survey, choices):
    answer = []
    
    index = [[0, 0] for _ in range(4)] # 각 지표별 최종 점수 예) index[0]은 1번 지표(R vs T)
    
    for i in range(len(survey)):
        idx = survey[i] # 현재 지표
        choice = choices[i] # 선택한 점수
        
        if idx == "RT" or idx == "TR": # 1번 지표
            index_n = 0
            first = 'R'
        elif idx == "CF" or idx == "FC":
            index_n = 1
            first = 'C'
        elif idx == "JM" or idx == "MJ":
            index_n = 2
            first = 'J'
        else:
            index_n = 3
            first = 'A'
        
        if choice <= 3: # 비동의에 해당하면 idx[0] 요소에 점수
            score = 4 - choice
            if idx[0] == first:
                index[index_n][0] += score
            else:
                index[index_n][1] += score
        elif choice > 4:
            score = choice - 4
            if idx[0] == first:
                index[index_n][1] += score
            else:
                index[index_n][0] += score
    
    for i in range(4):
        if i == 0:
            if index[i][0] >= index[i][1]:
                answer.append('R')
            else:
                answer.append('T')
        elif i == 1:
            if index[i][0] >= index[i][1]:
                answer.append('C')
            else:
                answer.append('F')
        elif i == 2:
            if index[i][0] >= index[i][1]:
                answer.append('J')
            else:
                answer.append('M')
        else:
            if index[i][0] >= index[i][1]:
                answer.append('A')
            else:
                answer.append('N')
    return ''.join(answer)