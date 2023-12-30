def solution(today, terms, privacies):
    answer = []
    
    today = today.split(".")
    
    # terms_dict {약관 종류 : 유효기간}
    terms_dict = {}
    for i in range(len(terms)):
        term = terms[i].split(" ")
        terms_dict[term[0]] = term[1]
    
    # privacies 순회
    for i in range(len(privacies)):
        privacy = privacies[i].split(" ") # privacy [수집된 날짜, 약관 종류]
        limit = int(terms_dict[privacy[1]]) # privacy[1]: 약관 종류 # 유효기간
        collected_date = privacy[0].split(".")
        
        collected_date[0] = int(collected_date[0])
        collected_date[1] = int(collected_date[1]) + limit
        collected_date[2] = int(collected_date[2]) - 1
        if collected_date[2] == 0:
            collected_date[1] -= 1
            collected_date[2] = 28
        while collected_date[1] > 12:
            collected_date[0] += 1
            collected_date[1] -= 12
            
        if int(today[0]) > collected_date[0]:
            answer.append(i+1)
        elif int(today[0]) == collected_date[0]:
            if int(today[1]) > collected_date[1]:
                answer.append(i+1)
            elif int(today[1]) == collected_date[1]:
                if int(today[2]) > collected_date[2]:
                    answer.append(i+1)
        
    return answer